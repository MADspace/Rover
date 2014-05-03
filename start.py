import server.http, server.rover, math, threading, time, subprocess

rover = server.rover.Rover()

def update_rover():
    while True:
        time.sleep(0.1)
        rover.update()

subprocess.Popen('LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -o "output_http.so -w /usr/local/www" -i input_uvc.so', shell=True)

thread = threading.Thread(target=update_rover)
thread.daemon = True
thread.start()

server.http.start_webapp(rover)
