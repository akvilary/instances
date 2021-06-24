from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Helvetica", 24, "bold")
SCORE_COLOR = 'white'

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color(SCORE_COLOR)
        self.goto(position)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)