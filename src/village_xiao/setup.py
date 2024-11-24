from setuptools import find_packages, setup
#导入glob，os模块，用于添加launch文件
from glob import glob
import os

package_name = 'village_xiao'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        #将launch文件放到install/package_name/share/package_name/launch目录下
        (os.path.join('share', package_name, 'launch'), glob('launch/*_launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='xq',
    maintainer_email='xq@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "xiao4_node = village_xiao.xiao4:main",#xiao4_node是节点名称，main是节点的主函数,启动节点的定义指令
            "xiao3_node = village_xiao.xiao3:main",#xiao3_node是节点名称，main是节点的主函数,启动节点的定义指令
        ],
    },
)

#creat package village_xiao that rely on rclpy
#ros2 pkg create village_xiao --build-type ament_python --dependencies rclpy