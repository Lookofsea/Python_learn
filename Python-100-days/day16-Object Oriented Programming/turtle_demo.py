from turtle import Turtle
from random import random

t = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.fillcolor("red")
    t.pencolor("green")
    t.right(angle)
    t.fd(steps)

t.screen.mainloop()