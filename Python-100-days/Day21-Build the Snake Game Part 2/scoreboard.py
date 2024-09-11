from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("consolas", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("Arial", 24, "normal"))
        

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    def get_score(self):
        return self.score