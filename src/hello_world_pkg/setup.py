from setuptools import find_packages, setup

package_name = 'hello_world_pkg'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='博客《同样是Python，为什么ROS2代码看起来完全不一样》配套示例',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            # ros2 run hello_world_pkg hello_world 就是从这里来的
            'hello_world = hello_world_pkg.hello_world_node:main',
        ],
    },
)
