from glob import glob
import os
from setuptools import find_packages, setup

package_name = 'py_pubsub'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
        ['resource/' + package_name]),
    ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros',
    maintainer_email='ros@todo.todo',
    description='Simple ROS 2 pub/sub example',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = py_pubsub.publisher:main',
            'listener = py_pubsub.subscriber:main',
            'number_publisher = py_pubsub.number_publisher:main',
            'number_subscriber = py_pubsub.number_subscriber:main',
            'position_publisher = py_pubsub.custom_coordinates_publisher:main',
            'distance_calculator = py_pubsub.distance_calculator:main',
            'boolean_toggle_publisher = py_pubsub.boolean_toggle_publisher:main',
            'toggle_counter = py_pubsub.boolean_toggle_counter:main',
            'noisy_sensor_data = py_pubsub.noisy_sensor_publisher:main',
            'noisy_temp_info = py_pubsub.noisy_sensor_temp_subscriber:main',
            'lr_subscriber = py_pubsub.left_right_subscriber:main',
            'right_command_pub = py_pubsub.right_command_pub:main',
            'left_command_pub = py_pubsub.left_command_pub:main',
            'transform_node = py_pubsub.raw_data_sub_tf_publisher:main',
        ],
    },
)