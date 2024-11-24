from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    xiao4_node = Node(package='village_xiao', executable='xiao4_node')
    li2_node = Node(package='village_li', executable='li2_node')
    return LaunchDescription([xiao4_node, li2_node])