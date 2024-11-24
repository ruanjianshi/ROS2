import rclpy 
from rclpy.node import Node

"""
    ros2运行该节点的入口函数
    编写ROS2节点的一般步骤
    1. 导入库文件
    2. 初始化客户端库
    3. 新建节点对象
    4. spin循环节点
    5. 关闭客户端库
    """
def main(args=None):
    rclpy.init(args=args)
    xiao4_node = Node("xiao4")
    xiao4_node.get_logger().info("Hello,goodmorning everybody,I'm xiao4 that is a writer")
    rclpy.spin(xiao4_node)
    rclpy.shutdown()