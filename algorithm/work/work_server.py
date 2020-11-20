import rospy
from common_msg.srv import battery, batteryResponse

def service_callback(request):
    response = batteryResponse(remain=request.all - request.run)
    print "request data:", request.all, request.run, ", response:", response.remain
    return response

rospy.init_node('work_server')
service = rospy.Service('battery', battery, service_callback)
rospy.spin()
