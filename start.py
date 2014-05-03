#!/usr/bin/python

import server.http, math, threading, time, subprocess, os
from server.rover import Rover, Servo

s = Servo(11, 1.4 / 1000, 1.1 / 1000)
s.set_rotation(0.0)

# Add this directory to the path
#os.chdir(os.path.dirname(__file__))

rover = Rover()

def update_rover():
    while True:
        time.sleep(Rover.UPDATE_PERIOD)
        rover.update()

subprocess.Popen('LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_uvc.so', shell=True)

thread = threading.Thread(target=update_rover)
thread.daemon = True
thread.start()

server.http.start_webapp(rover)
