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
    msg.vect = Vector3(x=second%4, y=second%7, z=second%5)
    pub.publish(msg)
    print "publish:", msg.timestamp.secs%100, msg.vect.x, msg.vect.y, msg.vect.z
    rate.sleep()


