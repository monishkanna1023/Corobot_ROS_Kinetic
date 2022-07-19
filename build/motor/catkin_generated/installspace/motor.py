#!/usr/bin/env python2
import roslib, rospy
from Phidget22.Phidget import *
from Phidget22.Devices.DCMotor import *
import tty, sys, termios

import time



def main():

	dcMotor0 = DCMotor()
	dcMotor1 = DCMotor()


	dcMotor0.setChannel(0)
	dcMotor1.setChannel(1)



	dcMotor0.openWaitForAttachment(5000)
	dcMotor1.openWaitForAttachment(5000)


	filedescriptors = termios.tcgetattr(sys.stdin)
	tty.setcbreak(sys.stdin)
	while 1:
		x=sys.stdin.read(1)[0]

		if x == "w":
			print("moving forward")
			dcMotor0.setTargetVelocity(0.1)
			dcMotor1.setTargetVelocity(0.1)
		if x == "s":
			print("moving reverse")
			dcMotor0.setTargetVelocity(-0.1)
			dcMotor1.setTargetVelocity(-0.1)
		if x == "q":
			print("stop")
			dcMotor0.setTargetVelocity(0.0)
			dcMotor1.setTargetVelocity(0.0)
		if x == "o":
			print("off")
			dcMotor0.setTargetVelocity(0)
			dcMotor1.setTargetVelocity(0)
			dcMotor0.close()
			dcMotor1.close()
			break
	termios.tcsetattr(sys.stdin, termios.TCSADRAIN,filedescriptors)
	


main()
