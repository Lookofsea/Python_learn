#my_snake_game

import turtle
import time
import random
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the screen
wn = turtle.Screen()
wn.title("My Snake Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


# Snake food
food = Food()
Scoreboard = Scoreboard()


snake = Snake()
# Keyboard bindings
wn.listen()
wn.onkeypress(snake.go_up, "Up")
wn.onkeypress(snake.go_down, "Down")
wn.onkeypress(snake.go_left, "Left")
wn.onkeypress(snake.go_right, "Right")

game_is_on = True
# Main game loop
while game_is_on:
    wn.update()
    time.sleep(0.1)
    snake.move()
    
    # Check if snake has eaten food
    # food is 10 * 10 square
    if snake.head.distance(food) < 10:
        food.refresh()
        
    # check if snake has collided with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        Scoreboard.game_over()
        game_is_on = False
        
    # check if snake has collided with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            Scoreboard.game_over()






