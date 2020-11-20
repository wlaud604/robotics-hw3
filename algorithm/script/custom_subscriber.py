import rospy
from common_msgs.msg import TimePose

def callback(msg):
    print "subscribe:", msg.timestamp.secs%100, msg.vect.x, msg.vect.y, msg.vect.z

rospy.init_node('custom_subscriber')
sub = rospy.Subscriber('custom_msg', TimePose, callback)
rospy.spin()
