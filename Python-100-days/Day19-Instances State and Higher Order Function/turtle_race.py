from random import randint
from turtle import Turtle, Screen

screen = Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

screen.setup(width=500, height=400)

user_choose = screen.textinput(title="Turtle Race",prompt="Enter your color: ")


# add finish line
finish_line = Turtle()
finish_line.color("black")
finish_line.penup()
finish_line.goto(200, 0)
finish_line.pendown()
finish_line.goto(200, 200)
finish_line.goto(200,-220)

is_race_on = False


for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(-200, i*50-100)
    turtles.append(turtle)

if user_choose:
    is_race_on = True

while is_race_on:
    for i in range(6):
        if turtles[i].xcor() > 200:
            is_race_on = False
            winner = turtles[i].pencolor()
            print(f"The winner is {winner}!")

        turtles[i].forward(randint(0,10))

screen.exitonclick()