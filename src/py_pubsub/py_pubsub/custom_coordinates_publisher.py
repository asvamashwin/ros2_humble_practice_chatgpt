# ✅ Problem 3: Custom 2D Coordinates
# Goal: Use a custom message with two float fields x, y.

# Create a custom .msg file in your package:
# Position2D.msg:

# go
# Copy
# Edit
# float32 x
# float32 y
# Publish random x, y values between 0–100

# Topic: /position

import rclpy
from rclpy.node import Node
from ros2_interfaces.msg import Position2D
import random

class CustomCoordinatesPublisher(Node):
    def __init__(self):
        super().__init__('position_publisher')
        self.publisher = self.create_publisher(Position2D, 'position', 10)
        self.timer = self.create_timer(1.0, self.publish_random_position)

    def publish_random_position(self):
        msg = Position2D()
        msg.x = random.uniform(0, 100)
        msg.y = random.uniform(0, 100)
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing Position: x={msg.x}, y={msg.y}')


def main(args=None):
    rclpy.init(args=args)
    custom_coordinates_publisher = CustomCoordinatesPublisher()
    rclpy.spin(custom_coordinates_publisher)
    custom_coordinates_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()