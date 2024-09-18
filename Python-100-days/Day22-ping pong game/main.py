from turtle import Screen, Turtle
import time
from player import Player
from ball import Ball
from scoreboard import Scoreboard

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
sccoreboard = Scoreboard()

screen.listen()

# Move the player
screen.onkey(right_player.move_up, "Up")
screen.onkey(right_player.move_down, "Down")

screen.onkey(left_player.move_up, "w")
screen.onkey(left_player.move_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with player
    if ball.distance(left_player) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.speed_up()

    if ball.distance(right_player) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.speed_up()

    # Detect when the game is over
    if ball.xcor() > 380:
        sccoreboard.l_point()
        ball.reset_position()

    if ball.xcor() < -380:
        sccoreboard.r_point()
        ball.reset_position()





screen.exitonclick()
