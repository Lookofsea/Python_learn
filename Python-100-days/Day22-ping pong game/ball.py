import turtle
class Ball(turtle.Turtle):
    def __init__(self):    
        super().__init__()
        self.shape("circle")
        self.penup()
        self.goto(0,0)
        
        self.speed(0)
        self.dx = 10
        self.dy = 10
        self.color("white")
        self.score = 0
        self.move_speed = 1.2

    def move(self):
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        #print(new_x,new_y)
        self.goto(new_x,new_y)

    def bounce_x(self):
        self.dx *= -1

    def bounce_y(self):
        self.dy *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.dx = 10
        self.dy = 10
        self.dx *= -1
    
    def speed_up(self):
        self.dx *= self.move_speed
        self.dy *= self.move_speed




