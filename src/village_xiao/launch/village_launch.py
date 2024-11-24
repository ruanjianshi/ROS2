from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Launch 启动节点定义
    xiao4_node = Node(
                      # 节点包名称
                      package='village_xiao', 
                      # 节点启动名称
                      executable='xiao4_node', 
                      # 节点命名空间
                      namespace='village_xiao',
                      # 节点参数设置，定义可调节的参数
                      parameters=[{"writer_timer_period": 1}])
    

    li2_node = Node(package='village_li', 
                    namespace='village_li',
                    executable='li2_node')
    
    #可接受多个启动组件，将多个节点启动描述返回给调用者
    return LaunchDescription([xiao4_node, li2_node])

# 启动指令：ros2 launch package_name village_launch.py