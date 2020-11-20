#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Vector3
from common_msgs.msg import TimePose

rospy.init_node('custom_publisher')
pub = rospy.Publisher('custom_msg', TimePose, queue_size=1)
msg = TimePose()
rate = rospy.Rate(1)
while not rospy.is_shutdown():
    msg.timestamp = rospy.get_rostime()
    second = msg.timestamp.secs
    msg.pose = Vector3(x=second.radint(1,100), y=second.randint(1,100), z=0)
    msg.pose.z = msg.pose.x * msg.pose.y 
    pub.publish(msg)
    print("X * Y = Z ")
    print ("publish:", msg.timestamp.secs%100, msg.pose.x, msg.pose.y, msg.pose.z)
    rate.sleep()


