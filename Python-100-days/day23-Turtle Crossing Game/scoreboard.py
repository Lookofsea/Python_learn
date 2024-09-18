FONT = ("Arial", 20, "bold")

class Scoreboard:
    def __init__(self):
        self.score = 0
        self.high_score = 0

    def update_score(self, score):
        self.score = score
        if self.score > self.high_score:
            self.high_score = self.score

    def draw_scoreboard(self, turtle):
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(-200, 250)
        turtle.write(f"Score: {self.score}", align="center", font=FONT)
        turtle.goto(-200, 200)
        turtle.write(f"High Score: {self.high_score}", align="center", font=FONT)   