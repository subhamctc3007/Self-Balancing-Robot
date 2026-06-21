from setuptools import find_packages, setup

package_name = 'balance_bot_control'

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
    maintainer='subham',
    maintainer_email='subhambtech22@vssut.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'imu_monitor = balance_bot_control.imu_monitor:main',
            # 'pid_controller = balance_bot_control.pid_controller:main',
        ],
    },
)
