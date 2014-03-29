import server.http, server.rover, math

rover = server.rover.Rover()

server.http.start_webapp(rover)
