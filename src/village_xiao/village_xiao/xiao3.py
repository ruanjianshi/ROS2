import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from village_interface.srv import Borrowmoney

class BaiPiaoNode(Node):

    def __init__(self,name):
        super().__init__(name)
        self.get_logger().info("大家好，我是xiao3，xiao4他哥，我可以白嫖xiao4小说！")
        self.sub_ = self.create_subscription(String,"sexy_girl",self.recv_callback,10)

        self.borrow_client = self.create_client(Borrowmoney,"borrowmoney")

    def recv_callback(self,novel):
        self.get_logger().info("xiao3 already receive %s" % novel.data)

    def borrow_money_eat(self,money=10):
        self.get_logger().info("borrow money to eat ,borrow %d" % money)
        while not self.borrow_client.wait_for_service(1.0):
            self.get_logger().info("please waiting ...")
        request = Borrowmoney.Request()
        request.name = self.get_name()
        request.money = money

        self.borrow_client.call_async(request).add_done_callback(self.borrow_response_callback)

    def borrow_response_callback(self,response):
        result = response.result()
        if result.success:
            self.get_logger().info("borrow money %d"%result.money)
        else:
            self.get_logger().info("no borrow money......")


def  main(args = None):
    rclpy.init(args=args)
    node = BaiPiaoNode("xiao3")
    node.borrow_money_eat()
    rclpy.spin(node)
    rclpy.shutdown()
