import turtle

DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # Snake head
        head = turtle.Turtle()
        head.speed(0)
        head.shape("square")
        head.color("white")
        head.penup()
        head.goto(0, 0)
        head.direction = "stop"
        self.segments.append(head)

    def move(self):
        for segment in range(len(self.segments)-1, 0, -1):
            x = self.segments[segment-1].xcor()
            y = self.segments[segment-1].ycor()
            self.segments[segment].goto(x, y)
        self.head.forward(DISTANCE)


        # Functions
    def go_up(self):
        if self.head.direction!= "down":
            self.head.direction = "up"
            self.head.setheading(90)

    def go_down(self):
        if self.head.direction!= "up":
            self.head.direction = "down"
            self.head.setheading(270)

    def go_left(self):
        if self.head.direction!= "right":
            self.head.direction = "left"
            self.head.setheading(180)

    def go_right(self):
        if self.head.direction!= "left":
            self.head.direction = "right"
            self.head.setheading(0)


