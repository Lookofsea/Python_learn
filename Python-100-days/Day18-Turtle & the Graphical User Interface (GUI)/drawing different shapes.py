import random
import turtle

# create a turtle object
t = turtle.Turtle()

# set the pen size
t.pensize(2)

def draw_shape(sides):
    degrees = 360/sides
    t.color(random.choice(['red', 'green', 'blue', 'yellow', 'purple']))
    for i in range(sides):
        t.forward(100)
        t.right(degrees)
    sides += 1


for nums_sides in range(3, 10):
    draw_shape(nums_sides)

# move the turtle to the center of the screen
t.penup()
t.goto(0, 0)
t.pendown()


# hide the turtle
t.hideturtle()

# keep the window open until clicked
turtle.done()