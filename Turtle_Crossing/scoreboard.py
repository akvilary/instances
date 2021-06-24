from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280, 260)
        self.level = 1
        self.level_info()

    def level_info(self):
        self.write(f"Level:{self.level}", align='left', font=FONT)

    def add_level(self):
        self.level += 1
        self.clear()
        self.level_info()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)
