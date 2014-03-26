import time, Queue, math
import servo

class Servo(object):
    # Rotation servo parameters
    center_rotation_pulse = 1.5 / 1000
    quarter_rotation_pulse = 0.5 / 1000

    # Continuous servo parameters
    stopped_speed_pulse = 1.5 / 1000
    full_speed_pulse = 0.5 / 1000 # Amount of pulse duration to add/subtract to the stopped_speed_pulse to get the servo to reach it maximum speed
    max_rotations_per_second = 60 / 60 # Rotation speed at maximum speed

    def __init__(self, channel):
        self.channel = channel

    def set_rotation(self, radians):
        if radians < -math.pi/2 or radians > math.pi/2:
            raise Exception("Servo can only rotate between -90 and 90 degrees")

        pulse_duration = radians / (math.pi / 2) * Servo.quarter_rotation_pulse + Servo.center_rotation_pulse
        servo.set_value(self.channel, pulse_duration)

    def set_speed(self, rotations_per_second):
        if math.abs(rotations_per_second) > max_rotations_per_second:
            raise Exception("Servo cannot rotate at %f rpm. Max rpm is %f" % (rpm, Servo.max_rotations_per_second))

        pulse_duration = rotations_per_second / Servo.max_rotations_per_second * Servo.full_speed_pulse + Servo.stopped_speed_pulse
        servo.set_value(self.channel, pulse_duration)


class Wheel(object):
    diameter = 0.092569 # in meters
    circumference = Wheel.diameter * math.pi

    """
    Represents one of the six wheels of the rover.
    All wheels have a driving servo inside the wheel for forward and backwards movement
    The four corner wheels also have a steering servo for rotating the wheel left and right.
    """

    def __init__(self, servo_drive, servo_steer, position_x, position_y):
        self.servo_drive = servo_drive
        self.servo_steer = servo_steer
        self.position_x = position_x
        self.position_y = position_y
        self.speed = 0
        self.rotation = 0

    def as_dict(self):
        return {'speed': self.speed, 'rotation': self.rotation, 'x': self.position_x, 'y': self.position_y}

    """
    Sets the rotation of the wheel in radians
    A positive value orients the wheel to the right, while a negative value turns it to the left
    """
    def set_rotation(self, radians):
        if self.servo_steer:
            self.rotation = radians
            pass # TODO
        else:
            raise "This wheel cannot be rotated"

    """
    Set the wheel in a straight forward moving position (no turning)
    """
    def straight(self):
        self.set_rotation(0)


    """
    Sets the forward moving speed of the wheel
    in meters per second
    """
    def set_speed(self, speed):
        self.speed = speed
        pass # TODO

    """
    Stop the wheel dead in its track
    """
    def stop(self):
        self.set_speed(0)

class DriveTrain:
    ROTATION_SPEED = 0.1

    def __init__(self):
        self.front_left   = Wheel(Servo(1), Servo(2), 0, 0)
        self.center_left  = Wheel(Servo(3), None, 0, 0)
        self.back_left    = Wheel(Servo(4), Servo(5), 0, 0)
        self.front_right  = Wheel(Servo(6), Servo(7), 0, 0)
        self.center_right = Wheel(Servo(8), None, 0, 0)
        self.back_right   = Wheel(Servo(9), Servo(10), 0, 0)

    def as_dict(self):
        return {'front_left': self.front_left.as_dict(),
                'center_left': self.center_left.as_dict(),
                'back_left': self.back_left.as_dict(),
                'front_right': self.front_right.as_dict(),
                'center_right': self.center_right.as_dict(),
                'back_right': self.back_right.as_dict(),
                }
    """

    """
    def drive(self, speed, turning_radius):
        pass

    def rotate(self, radians):
        pass

    def stop(self):
        self.front_left.stop()
        self.center_left.stop()
        self.back_left.stop()
        self.front_right.stop()
        self.center_right.stop()
        self.back_right.stop()

    def speed(self, speed):
        self.front_left.set_speed(speed)
        self.center_left.set_speed(speed)
        self.back_left.set_speed(speed)
        self.front_right.set_speed(speed)
        self.center_right.set_speed(speed)
        self.back_right.set_speed(speed)

    def straight(self):
        self.front_left.straight()
        self.back_left.straight()
        self.front_right.straight()
        self.back_right.straight()

class Rover:

    def __init__(self):
        self.command_queue = Queue.Queue()
        self.drivetrain = DriveTrain()

    def update(self):
        pass

    def as_dict(self):
        return {'drivetrain': self.drivetrain.as_dict()}


class Command:
    pass


