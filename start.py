import server.http, server.rover, math

rover = server.rover.Rover()
rover.control_joystick(0.5, 0.7, 0.0)

#rover.drivetrain.front_left.set_rotation(math.pi / 8)
#rover.drivetrain.front_right.set_rotation(-math.pi / 8)
#rover.drivetrain.back_left.set_rotation(-math.pi / 8)
#rover.drivetrain.back_right.set_rotation(math.pi / 8)

if False:
    rover.drivetrain.front_left.set_speed(0.3)
    rover.drivetrain.center_left.set_speed(0.3)
    rover.drivetrain.back_left.set_speed(0.3)
    rover.drivetrain.front_right.set_speed(0.3)
    rover.drivetrain.center_right.set_speed(0.3)
    rover.drivetrain.back_right.set_speed(0.3)


#from server.servo.servo import set_value
#set_value(0, 1.669 / 1000)
#set_value(2, 1.685 / 1000)
#set_value(3, 1.67 / 1000)


#server.http.start_webapp(rover)
