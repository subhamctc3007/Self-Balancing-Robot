from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch_ros.actions import Node
from launch.actions import TimerAction

from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():

    pkg_share = get_package_share_directory('balance_bot_description')

    # Include your existing URDF launch
    urdf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg_share, 'launch', 'urdf.launch.py')
        ),
        launch_arguments={
            'use_sim_time': 'true',
        }.items()
    )

    # Spawn robot into Gazebo (gz sim)
    spawn = TimerAction(
        period=1.0,
        actions=[
            Node(
                package='ros_gz_sim',
                executable='create',
                arguments=[
                    '-name', 'balance_bot',
                    '-topic', '/robot_description',
                    '-x', '0.0', # set these as per your world
                    '-y', '0.0',
                    '-z', '0.051', # little more than ground clearance. refer bot.urdf.xacro
                ],
                output='screen'
            )
        ]
    )

    controller_manager = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["diff_drive_controller"],
    )

    joint_state_broadcaster = Node(
        package="controller_manager",
        executable="spawner",
        arguments=["joint_state_broadcaster"],
    )

    twist_to_stamped_adapter = Node(
        package='balance_bot_description',
        executable='twist_to_stamped',
        output='screen',
    )

    teleop = Node(
        package='teleop_twist_keyboard',
        executable='teleop_twist_keyboard',
        name='teleop_twist_keyboard',
        prefix='xterm -e',  # opens teleop in a separate window
        output='screen',
        parameters=[
            {'stamped': False}
        ],
    )

    return LaunchDescription([
        urdf_launch,
        spawn,
        controller_manager,
        joint_state_broadcaster,
        # twist_to_stamped_adapter,
        # teleop,
    ])