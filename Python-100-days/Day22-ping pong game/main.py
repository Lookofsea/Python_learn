from turtle import Screen, Turtle
import time
from player import Player
from ball import Ball

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.tracer(0)

# Create the player
left_player = Player((-350, 0))
right_player = Player((350, 0))
ball = Ball()

screen.update()

screen.listen()

# Move the player
screen.onkey(left_player.move_up, "Up")
screen.onkey(left_player.move_down, "Down")

screen.onkey(right_player.move_up, "w")
screen.onkey(right_player.move_down, "s")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()


screen.exitonclick()