import time
from turtle import Turtle, Screen
from player import Player

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Game")

screen.tracer(0)


player = Player()
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

screen.exitonclick()