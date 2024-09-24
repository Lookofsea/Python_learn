COLORS = ['red', 'green', 'blue', 'yellow', 'purple', 'orange']
STARING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LEVEL = 1 # The higher the level, the more cars will be created

import random
from turtle import Turtle
class CarManager:
    def __init__(self, screen):
        self.screen = screen
        self.cars = []
        self.create_car()

    def create_car(self):
        random_chance = random.randint(1, 7 - LEVEL)
        if random_chance == 1:
        
            car = Turtle(shape='square')
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARING_MOVE_DISTANCE)
            if car.xcor() < -300:
                self.cars.remove(car)
                self.create_car()
            else:
                car.forward(MOVE_INCREMENT)
                
    def leve_up(self):
        global LEVEL
        LEVEL += 1