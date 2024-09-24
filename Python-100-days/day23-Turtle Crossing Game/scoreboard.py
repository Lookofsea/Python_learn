from turtle import Turtle
FONT = ("Arial", 20, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.draw_scoreboard(self)

    def draw_scoreboard(self):
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)
        
    def update_scoreboard(self):
        self.clear()
        self.draw_scoreboard(self)
        
    def increase_level(self):
        self.level += 1
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)
        self.goto(0, -20)
        self.write("Press 'r' to play again", align="center", font=FONT)
 