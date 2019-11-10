cmake_minimum_required(VERSION 2.8.3)
project(move_car)

## Compile as C++11, supported in ROS Kinetic and newer
##add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  geometry_msgs
  rospy
  visualization_msgs
)

catkin_package(
#  INCLUDE_DIRS include
#  LIBRARIES cctv_svm
#  CATKIN_DEPENDS OpenCV cv_bridge image_transport rospy sensor_msgs std_msgs
#  DEPENDS system_lib
)

include_directories(
 include
  ${catkin_INCLUDE_DIRS}
)

## Mark executable scripts (Python etc.) for installation
## in contrast to setup.py, you can choose the destination
install(PROGRAMS
  scripts/move_car
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
