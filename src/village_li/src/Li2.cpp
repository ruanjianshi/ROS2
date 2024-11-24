#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "std_msgs/msg/u_int32.hpp"
#include "village_interface/srv/sellnovel.hpp"
#include <queue>

using std::placeholders::_1;
using std::placeholders::_2;

class ReaderNode:public rclcpp::Node
{
private:
    rclcpp::Subscription<std_msgs::msg::String>::SharedPtr sub_novel;
    rclcpp::Publisher<std_msgs::msg::UInt32>::SharedPtr pub_money;

    std::queue<std::string> novels_queue;

    rclcpp::Service<village_interface::srv::Sellnovel>::SharedPtr sell_server;

    rclcpp::CallbackGroup::SharedPtr sell_novels_callback_group;

    unsigned int novel_price = 1;


    void novel_callback(const std_msgs::msg::String::SharedPtr novels)
    {
        std_msgs::msg::UInt32 money;
        money.data = 10;
        pub_money->publish(money);

        novels_queue.push(novels->data);

        RCLCPP_INFO(this->get_logger(),"already read %s",novels->data.c_str());
    }


    void sell_novels_callback(const village_interface::srv::Sellnovel::Request::SharedPtr request,
                             const village_interface::srv::Sellnovel::Response::SharedPtr response)
        {
            RCLCPP_INFO(this->get_logger(),"receive a request,money %d",request->money);

            this->get_parameter("novel_price",novel_price);


            unsigned int num = (int)(request->money/(novel_price));

            if(num>novels_queue.size())
            {
                RCLCPP_INFO(this->get_logger(),"book library no have %ld,< sell number book %d",novels_queue.size(),num);

                rclcpp::Rate rate(1);
                while(novels_queue.size()<num)
                {
                    RCLCPP_INFO(this->get_logger(),"waiting for book,%ld",num - novels_queue.size());
                    rate.sleep();
                }
            }
            else{

                RCLCPP_INFO(this->get_logger(),"book library have %ld,> sell number book %d",novels_queue.size(),num);

            }

            for(int i=0;i<(int)num;i++)
            {
                response->novels.push_back(novels_queue.front());
                novels_queue.pop();
            }


        }

public:
    ReaderNode(std::string name):Node(name)
    {
        RCLCPP_INFO(this->get_logger(),"Hello,I'm %s that is reader",name.c_str());

        sub_novel = this->create_subscription<std_msgs::msg::String>("sexy_girl",10,std::bind(&ReaderNode::novel_callback,this,_1));

        pub_money = this->create_publisher<std_msgs::msg::UInt32>("sexy_girl_money",10);

        sell_novels_callback_group = this->create_callback_group(rclcpp::CallbackGroupType::MutuallyExclusive);

        sell_server = this->create_service<village_interface::srv::Sellnovel>("sellnovel",
                                                                                std::bind(&ReaderNode::sell_novels_callback,this,_1,_2),
                                                                                rmw_qos_profile_services_default,
                                                                                sell_novels_callback_group);

        this->declare_parameter<std::int64_t>("novel_price",novel_price);
    }


};

int main(int argc, char ** argv)
{
    rclcpp::init(argc,argv);
    auto node = std::make_shared<ReaderNode>("Li2");

    rclcpp::executors::MultiThreadedExecutor executor;
    executor.add_node(node);
    executor.spin();
    //rclcpp::spin(node);
    rclcpp::shutdown();

}