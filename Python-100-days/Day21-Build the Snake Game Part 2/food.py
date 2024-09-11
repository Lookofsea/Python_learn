# 食物类
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x = -280 + random.randint(0, 560)
        y = -280 + random.randint(0, 560)
        self.goto(x, y)