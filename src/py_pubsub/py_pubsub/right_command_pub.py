import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class RightCommand(Node):
    def __init__(self):
        super().__init__('right_command_publisher')
        self.publisher = self.create_publisher(String, 'right_cmd', 10)
        self.timer = self.create_timer(1.0, self.right_cmd_pub)

    def right_cmd_pub(self):
        right_cmd = String()
        right_cmd.data = f'Take  RIGHT'
        self.publisher.publish(right_cmd)
        self.get_logger().info(f'publishing command {right_cmd.data}')

def main(args=None):
    rclpy.init(args=args)
    right_command_publisher = RightCommand()
    rclpy.spin(right_command_publisher)
    right_command_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()