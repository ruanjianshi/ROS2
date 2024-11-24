#include "rclcpp/rclcpp.hpp"
#include "village_interface/srv/sellnovel.hpp"

using std::placeholders::_1;
using std::placeholders::_2;

class PoorManNode: public rclcpp::Node
{

    public:
        PoorManNode(std::string name): Node(name)
        {
            RCLCPP_INFO(this->get_logger(), "PoorManNode has been created");

            novel_client = this->create_client<village_interface::srv::Sellnovel>("sellnovel");
        }

        void buy_novels()
        {
            RCLCPP_INFO(this->get_logger(), "Buying novels");

            while (!novel_client->wait_for_service(std::chrono::seconds(1)))
            {
                RCLCPP_INFO(this->get_logger(), "Waiting for service");
            }

            auto request = std::make_shared<village_interface::srv::Sellnovel_Request>();
            request->money = 5;
            novel_client->async_send_request(request, std::bind(&PoorManNode::novel_callback, this, _1));
            

        }
    private:

        rclcpp::Client<village_interface::srv::Sellnovel>::SharedPtr novel_client;

        void novel_callback(rclcpp::Client<village_interface::srv::Sellnovel>::SharedFuture reponse)
        {
            auto result = reponse.get();

            RCLCPP_INFO(this->get_logger(), "Received response from sellnovel service, chatter has %ld", result->novels.size());

            for(std::string novel: result->novels)
            {
                RCLCPP_INFO(this->get_logger(), "Novel: %s", novel.c_str());
            }

            RCLCPP_INFO(this->get_logger(), "Done with novels");
        }
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<PoorManNode>("zhang3");

    node->buy_novels();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}