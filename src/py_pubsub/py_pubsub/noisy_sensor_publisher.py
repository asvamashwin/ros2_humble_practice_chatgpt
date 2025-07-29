import rclpy
from rclpy.node import Node
from std_msgs.msg import Float32
import random

class NoisySensor(Node):
    def __init__(self):
        super().__init__('noisy_sensor_data')
        self.publisher = self.create_publisher(Float32, 'noisy_sensor_data', 10)
        self.timer = self.create_timer(1.0, self.publish_noisy_data)
    
    def publish_noisy_data(self):
        sensor_data = Float32()
        sensor_data.data = random.uniform(15,35)
        self.publisher.publish(sensor_data)
        self.get_logger().info(f'Temperature is : {sensor_data.data:.2f} degree celcius')

def main(args=None):
    rclpy.init(args=args)
    noisy_Sensor = NoisySensor()
    rclpy.spin(noisy_Sensor)
    noisy_Sensor.destroy_node()
    rclpy.shutdown()

if __name__ =='__main__':
    main()