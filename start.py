#import server.rover
import server.http, server.rover

rover = server.rover.Rover()

import server.servo
server.servo.set_value(0, 420)

server.http.start_webapp(rover)
