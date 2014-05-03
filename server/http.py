import web, sys, json

render = web.template.render('static')

class Debug:
    def GET(self):
        return open('static/index.html').read()

class Main:
    def GET(self, name):
        return open('static/mobile.html').read()

class Status:
    def GET(self):
        return json.dumps(rover.as_dict())

class Stop:
    def POST(self):
        rover.drivetrain.stop()

class Control:
    def POST(self):
        control_data = json.loads(web.data())
        if control_data['steer_axis'] <> '' and control_data['drive_axis'] <> '' and control_data['rotate_axis'] <> '':
            rover.control_joystick(float(control_data['steer_axis']), float(control_data['drive_axis']), float(control_data['rotate_axis']))

class Straight:
    def POST(self):
        rover.drivetrain.straight()

class Speed:
    def POST(self):
        rover.drivetrain.speed(float(web.data()))

class UpdateWheel:
    def POST(self, wheel_name):
        wheel_data = json.loads(web.data())
        wheel = getattr(rover.drivetrain, wheel_name)

        if 'center' not in wheel_name:
            wheel.set_rotation(float(wheel_data['rotation']))

        wheel.set_speed(float(wheel_data['speed']))


def start_webapp(rover):
    urls = (
        '/status', 'Status',
        '/control', 'Control',
        '/control/stop', 'Stop',
        '/control/straight', 'Straight',
        '/control/speed', 'Speed',
        '/update/wheel/(.+)', 'UpdateWheel',
        '/debug', 'Debug',
        '/(.*)', 'Main'
    )
    sys.modules[__name__].rover = rover

    app = web.application(urls, globals())
    web.httpserver.runsimple(app.wsgifunc(), ('0.0.0.0', 80))
