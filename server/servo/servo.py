from Adafruit_PWM_Servo_Driver import PWM

frequency = 60 # Frequency in Hz

pwm = PWM(0x40, debug=True)
pwm.setPWMFreq(frequency)

"""
Set the length of the pulse in seconds
"""
def set_value(channel, duration):
    period = 1 / frequency
    if duration > period:
        raise Exception("Cannot set duration to %f, period is only %f", duration, period)

    value = duration / period * 4096
    pwm.setPWM(channel, 0, int(value))
