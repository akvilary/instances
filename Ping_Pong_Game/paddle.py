from turtle import Turtle

PADDLE_COLOR = 'white'
PADDLE_SEGMENT_SHAPE = 'square'

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()

        #Coordinates
        self.y_position = 0
        if side == 'left':
            self.x_position = -350

        elif side == 'right':
            self.x_position = 350

        self.create_paddle(self.x_position, self.y_position)


    def create_paddle(self, x_position, y_position):
        x_pos = x_position
        y_pos = y_position
        self.shape(PADDLE_SEGMENT_SHAPE)
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color(PADDLE_COLOR)
        self.goto(x_pos, y_pos)


    def up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)


