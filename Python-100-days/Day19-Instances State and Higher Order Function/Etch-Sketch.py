#Make an Etch-A-Sketch App

import turtle

turtle = turtle.Turtle()
screen = turtle.getscreen()

def move_forward():
    turtle.forward(10)

def move_backward():
    turtle.backward(10)

def turn_left():
    turtle.left(10)

def turn_right():
    turtle.right(10)

def clear():
    turtle.clear()
    turtle.penup()
    turtle.home()


screen.onkey(move_forward, "Up")
screen.onkey(move_backward, "Down")
screen.onkey(turn_left, "Left")
screen.onkey(turn_right, "Right")

screen.onkey(clear, "c")


screen.listen()

screen.mainloop()