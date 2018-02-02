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
    for i in range (30, 160, 15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
    
    for i in range (150, 30, -15):
        setServoAngle(pan, i)
        setServoAngle(tilt, i)
        
    setServoAngle(pan, 100)
    setServoAngle(tilt, 90)    
    GPIO.cleanup()