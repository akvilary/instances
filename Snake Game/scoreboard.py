from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")
SCOREBOARD_COLOR = '#f5f5f5'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(0, 260)
        self.score_num = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.update_score()

    def reset_score(self):
        if self.score_num > self.high_score:
            self.high_score = self.score_num
            with open("data.txt", mode='w') as file:
                file.write(self.high_score))
        self.score_num = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score_num} | The highest score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score_num += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)