class Car:

  def __init__(self, engineisrunning = False, wheel_angle = 0, speed = 0):
      self.wheel_angle = wheel_angle
      self.speed = speed
      self.engineisrunning = engineisrunning

  def startengine(self):
      print("Vrmmm")
      self.engineisrunning = True

  def accelerate(self):
      if self.engineisrunning is True:
          accelerated_speed = 90
          self.speed =+ accelerated_speed
      #else:print("Engine needs to be running. ")

  def slowdown(self):
      pass

  def turn(self):
      self.wheel_angle = 135

  def obstacle(self):
      pass

  def stopengine(self):
      self.engineisrunning = False
      self.wheel_angle = 0
      self.speed = 0

  def act(self, event):
      if event == 'startengine':
         self.startengine()

      if event == 'accelerate':
         self.accelerate()

      if event == 'slowdown':
         self.slowdown()

      if event == 'turn_right':
         self.turn()

      #if event == 'turn_left':
         #self.wheel_angle = 45

      if event == 'stopengine':
         self.stopengine()

car = Car()

while True:

    carinput = input('I am a car, what should I do? ')

    if carinput == 'startengine':
        car.act('startengine')

    if carinput == 'accelerate':
        car.act('accelerate')
        print('Wheels angle is {}° and Speed is {}km/h'
        .format(car.wheel_angle, car.speed))

    if carinput == 'slowdown':
        car.act('slowdown')
        print('Wheels angle is {}° and Speed is {}km/h'
        .format(car.wheel_angle, car.speed))

    #if carinput == 'turn'
    #    pass

    if carinput == 'obstacle':
        car.act('obstacle')
        print('Wheels angle is {}° and Speed is {}km/h'
        .format(car.wheel_angle, car.speed))

    if carinput == 'stopengine':
        car.act('stopengine')
        print('Wheels angle is {}° and Speed is {}km/h'
        .format(car.wheel_angle, car.speed))

    if carinput == 'endtheloop':
        break
