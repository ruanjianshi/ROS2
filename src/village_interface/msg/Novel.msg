# 原始数据类型

string content

sensor_msgs/Image image

#1、基本数据类型:

#bool：布尔类型，表示真（true）或假（false）。
#byte：8位字节，通常用于存储原始数据。
#char：字符类型，表示一个字符。
#float32：32位浮点数，用于表示小数。
#float64：64位浮点数，更高精度的小数。
#int8：8位有符号整数。
#int16：16位有符号整数。
#int32：32位有符号整数。
#int64：64位有符号整数。
#uint8：8位无符号整数。
#uint16：16位无符号整数。
#uint32：32位无符号整数。
#uint64：64位无符号整数。
#string：字符串类型，用于存储文本数据。

#2、复合类型:

#数组：可以是任意数据类型的数组，如float32[]、int32[]等。
#用户自定义消息类型：用户可以定义自己的消息类型，组合基本数据类型和其他用户定义的消息。

#3、标准消息类型：

#ROS还定义了一些常用的标准消息类型，例如：
#std_msgs/String: 字符串消息。
#std_msgs/Int32: 整数消息。
#sensor_msgs/Image: 图像数据消息。
#geometry_msgs/Twist: 机器人速度信息。