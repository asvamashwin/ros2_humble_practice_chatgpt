import rclpy
from rclpy.node import Node
from ros2_interfaces.msg import BooleanToggle

class BooleanTogglePublisher(Node):
    def __init__(self):
        super().__init__('booleantoggle_publisher')
        self.publisher = self.create_publisher(BooleanToggle,'toggle_signal',10)
        self.create_timer = self.create_timer(1.0, self.toggle_boolean_publisher)
        self.flag = True
    def toggle_boolean_publisher(self):
        msg = BooleanToggle()
        msg.toggle = self.flag
        self.publisher.publish(msg)
        self.get_logger().info(f'Boolean Status: {msg.toggle}')
        self.flag = not msg.toggle


def main(args=None):
    rclpy.init(args=args)
    boolean_toggle_publisher = BooleanTogglePublisher()
    rclpy.spin(boolean_toggle_publisher)
    boolean_toggle_publisher.destroy_node()
    rclpy.shutdown()

if __name__  == '__main__' :
    main()