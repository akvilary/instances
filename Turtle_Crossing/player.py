from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
PLAYER_SHAPE = 'turtle'
PLAYER_COLOR = 'green'


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(PLAYER_SHAPE)
        self.color(PLAYER_COLOR)
        self.penup()
        self.setheading(90)
        self.position_refresh()
        self.finish_line = FINISH_LINE_Y

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True

    def position_refresh(self):
        self.goto(STARTING_POSITION)
