import rclpy
from rclpy.node import Node
from ros2_interfaces.msg import BooleanToggle

class ToggleCounter(Node):
    def __init__(self):
        super().__init__('boolean_toggle_counter')
        self.subscription = self.create_subscription(
            BooleanToggle,
            'toggle_signal',
            self.listener_callback,
            10,
        )
        self.previous_value = None
        self.toggle_count = 0
        self.subscription
    def listener_callback(self, msg):
        curr_val = msg.toggle
        if self.previous_value is None:
            self.previous_value = msg.toggle
            self.get_logger().info(
                f"Received {msg.toggle}"
            )
            return
        if msg.toggle != self.previous_value:
            self.toggle_count += 1
            self.get_logger().info(
                f"Received {msg.toggle} Toggled {self.toggle_count} times so far"
            )
            self.previous_value = msg.toggle
        
def main(args=None):
    rclpy.init(args=args)
    node = ToggleCounter()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
