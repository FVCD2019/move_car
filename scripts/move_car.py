#!/usr/bin/env python
import rospy
import numpy as np
import glob
import time
from sensor_msgs.msg import Image
from geometry_msgs.msg import PoseStamped
from visualization_msgs.msg import MarkerArray

class MOVE:
	def __init__(self):
		print("init")
		rospy.init_node('move_car', anonymous=True)
		self.move_pub = rospy.Publisher("move_base_simple/start", PoseStamped, queue_size=1)
		self.pose_sub = rospy.Subscriber("/pathVehicle", MarkerArray, self.poseCB)

		self.pose_x = None
		self.pose_y = None
		self.pose_z = None
		self.ori_z = None
		self.ori_w = None


	def poseCB(self, data):
		#print("hahaha")
		self.pose_x = data.markers[-1].pose.position.x
		self.pose_y = data.markers[-1].pose.position.y
		self.pose_z = data.markers[-1].pose.position.z
		self.ori_z = data.markers[-1].pose.orientation.z
		self.ori_w = data.markers[-1].pose.orientation.w

		if (self.pose_x != 0 and self.pose_y != 0):
			print(self.pose_x,self.pose_y)
			Move_point = PoseStamped()
			Move_point.header.stamp = rospy.Time.now()
			Move_point.header.frame_id = "map"
			Move_point.pose.position.x = self.pose_x
			Move_point.pose.position.y = self.pose_y
			Move_point.pose.position.z = self.pose_z
			Move_point.pose.orientation.x = 0.0
			Move_point.pose.orientation.y = 0.0
			Move_point.pose.orientation.z = self.ori_z
			Move_point.pose.orientation.w = self.ori_w
			self.move_pub.publish(Move_point)
			print("pub")
		else:
			print("zero")

	def movecar(self):
		# while not rospy.is_shutdown():
		# 	move_point = PoseStamped()
		# 	move_point.header.stamp = rospy.Time.now()
		# 	Move_point.header.frame_id = "map"
		# 	Move_point.pose.position.x = self.pose_x
		# 	Move_point.pose.position.y = self.pose_y
		# 	Move_point.pose.position.z = self.pose_z
		# 	Move_point.pose.orientation.x = 0.0
		# 	Move_point.pose.orientation.y = 0.0
		# 	Move_point.pose.orientation.z = self.ori_z
		# 	Move_point.pose.orientation.w = self.ori_w
		# 	move_pub.publish(Move_point)
		# 	print(self.x_val)
		rospy.spin()



Move = MOVE()
time.sleep(1)
Move.movecar()
