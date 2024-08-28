import turtle
import random

# set the screen size
turtle.setup(500, 500)

# set the pen color and size
turtle.pensize(5)

# set the turtle speed  
turtle.speed(0)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

turtle.colormode(255)
#random walk function
def random_walk():
    for i in range(100):
        # move the turtle forward by a random amount
        distance = 20
        turtle.forward(distance)
        turtle.color(random_color())
        # turn the turtle by a random amount
        angle = random.choice(directions)
        turtle.left(angle)  

# call the random_walk function
random_walk()

# hide the turtle
turtle.hideturtle()

# keep the window open until clicked
turtle.done()

