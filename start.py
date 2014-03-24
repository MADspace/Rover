import server.http, server.rover

rover = server.rover.Rover()

server.http.start_webapp(rover)
