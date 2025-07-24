# ✅ Problem 1: Number Publisher
# Goal: Create a publisher that sends increasing integers on the topic /numbers.

# Topic: /numbers

# Msg type: std_msgs/msg/Int32

# Frequency: 2 Hz

# Starts from 0, increments by 1 every message

import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class NumberPublisher(Node):
    def __init__(self):
        super().__init__('number_publisher')
        self.publisher_ = self.create_publisher(Int32, 'numbers', 10)
        timer_period = 0.5  # seconds (2 Hz)
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Int32()
        msg.data = self.i
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.i += 1

def main(args=None):
    rclpy.init(args=args)
    number_publisher = NumberPublisher()
    rclpy.spin(number_publisher)
    number_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()