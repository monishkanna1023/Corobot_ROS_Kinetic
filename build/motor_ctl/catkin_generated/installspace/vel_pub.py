#!/usr/bin/env python2
import rospy
from motor_ctl.msg import vel


def motor_ctl():
    vel_pub = rospy.Publisher('velocity_pub', vel, queue_size=10)
    rospy.init_node('motor', anonymous=True)
    rate = rospy.Rate(100) 
    while not rospy.is_shutdown():
        wheel_vel = vel()
        wheel_vel.lv = 0.2
        wheel_vel.rv = 0.2
        

        vel_pub.publish(wheel_vel)
        rate.sleep()
    while rospy.is_shutdown():
        wheel_vel = vel()
        wheel_vel.lv = 0
        wheel_vel.rv = 0
        

        vel_pub.publish(wheel_vel)
        break


if __name__ == '__main__':
    try:
        motor_ctl()
    except rospy.ROSInterruptException:
        pass
