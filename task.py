# Write a module that will simulate autonomic car.
# The simulation is event based, an example:
# car1 = Car()
# car1.act(event)
# print(car1.wheel_angle, car1.speed)
# where event can be anything you want, i.e. :
# `('obstacle', 10)` where `10` is a duration (time) of the event.
##The program should:
# - act on the event
# - print out current steering wheel angle, and speed
# - run in infinite loop
# - until user breaks the loop

#The level of realism in simulation is of your choice, but more sophisticated solutions are better.
#If you can thing of any other features, you can add them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to github repository.
#
#Delete these comments before commit!
#Good luck.

class Car:

  def __init__(self, wheel_angle = 0, speed = 0):
      self.wheel_angle = wheel_angle
      self.speed = speed

  def act(self, event):
      if event == 'turn_right':
         self.wheel_angle = 135

      if event == 'turn_left':
         self.wheel_angle = 45

      if event == 'accelerate':
         accelerated_speed = 90
         self.speed =+ accelerated_speed

      if event == 'stop':
         slowed_speed = 0
         self.speed =- slowed_speed

car1 = Car()
print(car1.wheel_angle, car1.speed)

car1.act('accelerate')
print(car1.wheel_angle, car1.speed)

car1.act('turn_right')
print(car1.wheel_angle, car1.speed)
