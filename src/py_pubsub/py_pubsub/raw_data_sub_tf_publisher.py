import rclpy
from rclpy.node import Node
from std_msgs.msg import Int32

class RawDataSubPub(Node):
    def __init__(self):
        super().__init__('transform_node')
        self.publisher = self.create_publisher(Int32, 'processed_data', 10)
        
        self.sub_to_raw_data = self.create_subscription(
            Int32,
            'raw_data',
            self.listener_sub_pub,
            10
        )
    def listener_sub_pub(self,msg):
        raw_val = msg.data
        processed_val = raw_val * 2

        new_msg = Int32()
        new_msg.data = processed_val
        # right_cmd.data = f'Take  RIGHT'
        self.publisher.publish(new_msg)
        self.get_logger().info(f'Received: {raw_val} ->  Publishing: {new_msg.data}')

def main(args=None):
    rclpy.init(args=args)
    raw_data_sub_publisher = RawDataSubPub()
    rclpy.spin(raw_data_sub_publisher)
    raw_data_sub_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()