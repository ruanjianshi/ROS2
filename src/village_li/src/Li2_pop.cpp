#include "rclcpp/rclcpp.hpp"


int main(int argc, char ** argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<rclcpp::Node>("Li2");
    RCLCPP_INFO(node->get_logger(),"Hello,I'm Li2 that is reader");
    rclcpp::spin(node);
    rclcpp::shutdown();

}