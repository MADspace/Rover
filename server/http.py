import web, sys, json

render = web.template.render('static')

class Main:
    def GET(self, name):
        return open('static/index.html').read()

class Status:
    def GET(self):
        return json.dumps(rover.as_dict())

class Stop:
    def POST(self):
        rover.drivetrain.stop()

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
            wheel.set_rotation(wheel_data['rotation'])

        wheel.set_speed(wheel_data['speed'])


def start_webapp(rover):
    urls = (
        '/status', 'Status',
        '/control/stop', 'Stop',
        '/control/straight', 'Straight',
        '/control/speed', 'Speed',
        '/update/wheel/(.+)', 'UpdateWheel',
        '/(.*)', 'Main'
    )
    sys.modules[__name__].rover = rover

    app = web.application(urls, globals())
    app.run()