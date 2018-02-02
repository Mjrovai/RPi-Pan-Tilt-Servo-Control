#!/usr/bin/env python
#
#  Pan Tilt Servo Control 
#  Execute with parameter ==> sudo python3 servoCtrl.py <pan_angle> <tilt_angle>
#
#  MJRoBot.org 01Feb18
  
from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pan = 27
tilt = 17

GPIO.setup(tilt, GPIO.OUT) # white => TILT
GPIO.setup(pan, GPIO.OUT) # gray ==> PAN

def setServoAngle(servo, angle):
	assert angle >=30 and angle <= 150
	pwm = GPIO.PWM(servo, 50)
	pwm.start(8)
	dutyCycle = angle / 18. + 3.
	pwm.ChangeDutyCycle(dutyCycle)
	sleep(0.3)
	pwm.stop()

if __name__ == '__main__':
	import sys
	if len(sys.argv) == 1:
		setServoAngle(pan, 90)
		setServoAngle(tilt, 90)
	else:
		setServoAngle(pan, int(sys.argv[1])) # 30 ==> 90 (middle point) ==> 150
		setServoAngle(tilt, int(sys.argv[2])) # 30 ==> 90 (middle point) ==> 150
	GPIO.cleanup()

