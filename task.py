import logging
from threading import Timer
from time import sleep

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:%(message)s')

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class Event:

    def __init__(self, name='', seconds=0, duration=0, avoidable=None):
        self.name = name
        self.seconds = seconds
        self.duration = duration
        self.avoidable = avoidable
        self.obstacle = ['pedestrian', 'dog', 'deer', 'wall']
        self.mode = ['city', 'highway']


class Car:

    def __init__(self, engine_running=False, wheel_angle=0, speed=0):
        self.wheel_angle = wheel_angle
        self.speed = speed
        self.engine_running = engine_running

        logger.info('Created object car with wheel angle: {}, speed: {} engine_running: {}'
                    .format(self.wheel_angle, self.speed, self.engine_running))

    def startengine(self):
        self.engine_running = True
        logger.info('Engine is running: {}'.format(self.engine_running))

    def accelerate(self, speed):
        if self.engine_running is True:
            if speed <= 200:
                self.speed += speed
                logger.info('Car speed: {}km/h, wheel angle: {}°'
                            .format(self.speed, self.wheel_angle))
            else: logger.error('Maximal speed of the car is 200km/h!')
        else: logger.error('The engine is not running!')

    def slowdown(self, speed):
        if self.engine_running is True:
            if speed >= 0:
                self.speed -= speed
                logger.info('Car speed: {}km/h, wheel angle: {}°'
                            .format(self.speed, self.wheel_angle))
            else: logger.error('The car speed must not be negative!')
        else: logger.error('The engine is not running!')

    def turn(self, angle):
        self.wheel_angle = (self.wheel_angle + angle) % 360
        logger.info('Car speed: {}km/h, wheel angle: {}°'
                    .format(self.speed, self.wheel_angle))

    def breaks(self):
        self.speed = 0
        logger.info('Car speed: {}km/h, wheel angle: {}°'
                    .format(self.speed, self.wheel_angle))

    def stopengine(self):
        self.engine_running = False
        self.wheel_angle = 0
        self.speed = 0

    def back2track(self):
        self.wheel_angle = 0
        logger.info('Wheel angle is back to normal: {}°'
                    .format(self.wheel_angle))

    def handle_obstacle(self, event, seconds):
        if event.name in event.obstacle and seconds > 20:
            event.avoidable = True
            self.turn(45)
            timer = Timer(10.0, self.back2track)
            timer.start()
        elif event.name in event.obstacle and seconds < 20:
            event.avoidable = False
            self.breaks()

    def handle_mode(self, event, duration):
        if event.name == 'city':
            if self.speed == 0:
                self.accelerate(50)
                sleep(event.duration)
            elif self.speed >= 50:
                self.speed = 50
                logger.info('Car speed: {}km/h, wheel angle: {}°'
                            .format(self.speed, self.wheel_angle))
                sleep(event.duration)
            elif self.speed < 50:
                self.accelerate(50 % self.speed)
                sleep(event.duration)
        elif event.name == 'highway':
            if self.speed == 0:
                self.accelerate(110)
                sleep(event.duration)
            elif self.speed >= 110:
                self.slowdown(self.speed % 110)
                sleep(event.duration)
            elif self.speed < 110:
                self.speed = 110
                logger.info('Car speed: {}km/h, wheel angle: {}°'
                            .format(self.speed, self.wheel_angle))
                sleep(event.duration)

    def __repr__(self):
        return 'Car speed: {}km/h, wheel angle: {}°'.format(self.speed,
                                                            self.wheel_angle)


def main():
    car = Car()
    car.startengine()
    car.accelerate(speed=30)
    while True:
        event = Event()
        event.name = input('What event should occur? ({}, {} and exit): '
                           .format(', '.join(event.obstacle), ', '.join(event.mode)))
        if event.name == 'exit':
            logger.info('Exiting program')
            break
        elif event.name in event.obstacle:
            event.seconds = int(input('How many seconds is the obstacle '
                                      'away from the car? '))
            car.handle_obstacle(event, event.seconds)
        elif event.name in event.mode:
            event.duration = int(input('For how long do you want to stay '
                                       'in this mode? '))
            car.handle_mode(event, event.duration)
        else: logger.error('This event does not exist.')


if __name__ == '__main__':
    main()
