from Adafruit_PWM_Servo_Driver import PWM

pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(60)

def set_value(channel, value):
    pwm.setPWM(channel, 0, value)
