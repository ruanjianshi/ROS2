import rclpy 
from rclpy.node import Node
from std_msgs.msg import String,UInt32
from village_interface.srv import Borrowmoney # type: ignore

#发布者创建过程
"""
    导入发布消息类型
    声明并创建发布者
    编写发布逻辑发布数据
"""
#订阅者创建过程
"""
    导入订阅消息类型
    声明并创建发布者
    编写发布者逻辑发布数据
"""
#节点NODE的创建过程
"""
    ros2运行该节点的入口函数
    编写ROS2节点的一般步骤
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点对象
    4. spin循环节点
    5. 关闭客户端库
"""
#服务端创建过程
"""
    1、导入服务接口
    2、创建服务端回调函数
    3、声明并创建服务端
    4、编写回调函数逻辑处理请求
"""
#客户端创建过程
"""
    1、导入服务接口
    2、创建请求结果接受回调函数
    3、声明并创建客户端
    4、编写结果接受逻辑
    5、调用客户端发送请求
"""

class WriterNode(Node):
    def __init__(self,name):
        #初始化节点
        super().__init__(name)
        #产生日志输出在终端，可便于观察效果
        self.get_logger().info("Hello,goodmorning everybody,I'm %s that is a writer" %name)
        #创建一个发布者对象，定义数据类型，名称，队列大小
        self.pub_novel = self.create_publisher(String,"sexy_girl",10)
        #定时器周期
        self.timer_period = 5
        #计数器初始化
        self.count = 0
        #创建一个定时器对象，定义循环时间，回调函数
        self.timer = self.create_timer(self.timer_period,self.timer_callback)
        #帐户余额初始化
        self.account = 80
        #创建一个订阅者对象，定义数据类型，名称，回调函数，队列大小
        self.sub_money = self.create_subscription(UInt32,"sexy_girl_money",self.recv_money_callback,10)
        #创建一个服务端服务对象，定义数据类型（自定义类型），名称，回调函数
        self.borrow_server = self.create_service(Borrowmoney,"borrowmoney",self.borrow_money_callback)

        #声明参数，参数名称，参数默认值
        self.declare_parameter("writer_timer_period",5)

    #定时器对象的回调函数，每循环定时结束，调用该函数
    def timer_callback(self):
        #获取参数值
        timer_period = self.get_parameter("writer_timer_period").get_parameter_value().integer_value
        #修改定时器周期
        self.timer.timer_period_ns = timer_period * (1000*1000*1000)
        #创建一个String类型的消息对象
        msg = String()
        #设置消息内容
        msg.data = "meet %d: calculate count %d"%(self.count,self.count)
        #发布消息
        self.pub_novel.publish(msg)
        #打印日志
        self.get_logger().info("publish a novel:context%s"%msg.data)
        #计数器加1
        self.count += 1

    #订阅者对象的回调函数，接受数据为UInt32,赋值给money
    def recv_money_callback(self,money):
        #帐户余额加上收到的钱
        self.account += money.data
        #打印日志
        self.get_logger().info("receive %d money,account %d money"%(money.data,self.account))
    #服务端服务对象的回调函数，接受数据为自定义类型，以---分割，前者数据赋给request,后者数据赋给response,通过.索引自定义数据的原始类型
    def borrow_money_callback(self,request,response):
        #打印日志
        self.get_logger().info("receive who money:%s , account %d  " %(request.name,self.account))
        #判断余额是否足够
        if request.money <= self.account*0.1:
            #余额足够，扣款，返回成功
            response.success = True
            #返回扣款金额
            response.money = request.money
            #扣款
            self.account = self.account - request.money
            #打印日志
            self.get_logger().info("borrow success,borrow %d,surplus %d"%(response.money,self.account))
            
        else:
            #余额不足，返回失败
            response.success = False
            #返回扣款金额
            response.money = 0
            #打印日志
            self.get_logger().info("sorry,don't borrow money")
        #返回响应
        return response


def main(args=None):
    #初始化ROS2节点
    rclpy.init(args=args)
    #创建节点对象
    xiao4_node = WriterNode("xiao4")
    #阻塞等待节点结束    
    rclpy.spin(xiao4_node)
    #关闭节点
    rclpy.shutdown()