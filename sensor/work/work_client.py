import rospy
from common_msgs.srv import battery, batteryRequest

rospy.init_node('work_client')
rospy.wait_for_service('battery')
requester = rospy.ServiceProxy('battery', battery)
print "requester type:", type(requester), ", callable?", callable(requester)
rate = rospy.Rate(10)
count=0
while count<100;
	 rep=battertRequest(all=100 ,run=count)
	 res=requester(req)
	 if res < 5;
	  print("Low battery")
	  break
	print count, "request:", req.all,req.run,"response:",res.remain
    rate.sleep()
    count += 1
 

