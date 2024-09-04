#my_snake_game

import turtle
import time
import random
from snake import Snake

# Set up the screen
wn = turtle.Screen()
wn.title("My Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)



snake = Snake()
# Keyboard bindings
wn.listen()
wn.onkeypress(snake.go_up, "Up")
wn.onkeypress(snake.go_down, "Down")
wn.onkeypress(snake.go_left, "Left")
wn.onkeypress(snake.go_right, "Right")


# Main game loop
while True:
    wn.update()
    time.sleep(0.1)
    snake.move()






