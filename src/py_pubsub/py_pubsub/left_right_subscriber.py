import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LeftRightSub(Node):
    def __init__(self):
        super().__init__('left_right_command_sub')
        self.sub_right = self.create_subscription(
            String,
            'right_cmd',
            self.right_callback,
            10
        )

        self.sub_left = self.create_subscription(
            String,
            'left_cmd',
            self.left_callback,
            10
        )

    def left_callback(self, msg):
        self.get_logger().info(f'LEFT message: {msg.data}')

    def right_callback(self, msg):
        self.get_logger().info(f'RIGHT message: {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    lr_subscriber = LeftRightSub()
    rclpy.spin(lr_subscriber)
    lr_subscriber.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
        main()