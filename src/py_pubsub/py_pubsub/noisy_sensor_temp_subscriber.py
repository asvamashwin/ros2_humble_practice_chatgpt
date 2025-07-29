import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
class TemperatureFilter(Node):
    def __init__(self):
        super().__init__('temperature_filter')
        self.subscription = self.create_subscription(
            Float32,
            'noisy_sensor_data',
            self.temp_filter,
            10
        )
        self.subscription

    def temp_filter(self, msg):
        if msg.data > 30:
            self.get_logger().info(f'received temperature higher than 30 !!! {msg.data}')

def main(args=None):
    rclpy.init(args=args)
    temp_filter = TemperatureFilter()
    rclpy.spin(temp_filter)
    temp_filter.destroy_node()
    rclpy.shutdown()