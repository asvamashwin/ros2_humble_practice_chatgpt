import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class LeftCommand(Node):
    def __init__(self):
        super().__init__('left_command_publisher')
        self.publisher = self.create_publisher(String, 'left_cmd', 10)
        self.timer = self.create_timer(1.0, self.left_cmd_pub)

    def left_cmd_pub(self):
        left_cmd = String()
        left_cmd.data = f'Take  LEFT'
        self.publisher.publish(left_cmd)
        self.get_logger().info(f'publishing command {left_cmd.data}')

def main(args=None):
    rclpy.init(args=args)
    left_command_publisher = LeftCommand()
    rclpy.spin(left_command_publisher)
    left_command_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()