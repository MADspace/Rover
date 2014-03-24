#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time, sys

pwm = PWM(0x40, debug=True)

print sys.argv
pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
pwm.setPWM(1, 0, int(sys.argv[1]))
