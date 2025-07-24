import rclpy
from rclpy.node import Node
from ros2_interfaces.msg import Position2D
import math

class DistanceCalculator(Node):
    def __init__(self):
        super().__init__('distance_calculator')
        self.subscription = self.create_subscription(
            Position2D,
            'position',
            self.listener_callback,
            10

        )
        self.subscription
    def listener_callback(self, msg):
        distance = math.sqrt(msg.x**2 +msg.y**2)
        self.get_logger().info(
            f"Received x={msg.x:.2f}, y={msg.y:.2f} -> Distance from (0,0): {distance:.2f}"
        )
def main(args=None):
    rclpy.init(args=args)
    node = DistanceCalculator()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()