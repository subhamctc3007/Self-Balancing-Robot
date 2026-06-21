#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from scipy.spatial.transform import Rotation

class ImuMonitor(Node):
    def __init__(self):
        super().__init__('imu_monitor')
        self.subscription = self.create_subscription(
            Imu,
            '/imu',
            self.imu_callback,
            10
        )
        self.get_logger().info('IMU Monitor Started')

    def imu_callback(self, msg):
        quat = [
            msg.orientation.x,
            msg.orientation.y,
            msg.orientation.z,
            msg.orientation.w
        ]
        rotation = Rotation.from_quat(quat)
        roll, pitch, yaw = rotation.as_euler('xyz', degrees=False)
        self.get_logger().info(f'Roll: {roll:.3f} | Pitch: {pitch:.3f} | Yaw: {yaw:.3f}')

def main(args=None):
    rclpy.init(args=args)
    node = ImuMonitor()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()