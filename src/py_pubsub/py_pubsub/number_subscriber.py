# ✅ Problem 2: Even Number Subscriber
# Goal: Subscribe to /numbers and only print even ones.

# Subscribe to: /numbers

# Check if msg.data % 2 == 0 before printing

# Expected log: "[Even] 4"
import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class EvenNumberSubscriber(Node):
    def __init__(self):
        super().__init__('even_number_subscriber')
        self.subscription = self.create_subscription(
            Int32,
            'numbers',
            self.listener_callback,
            10
        )
        self.subscription

    def listener_callback(self, msg):
        if msg.data % 2 == 0:
            self.get_logger().info(f'[Even] {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    even_number_subscriber = EvenNumberSubscriber()
    rclpy.spin(even_number_subscriber)
    even_number_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()