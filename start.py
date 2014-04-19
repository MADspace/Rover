import server.http, server.rover, math, threading, time

rover = server.rover.Rover()

def update_rover():
    while True:
        time.sleep(0.1)
        rover.update()

thread = threading.Thread(target=update_rover)
thread.daemon = True
thread.start()

server.http.start_webapp(rover)
