from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
LEFT = 180
DOWN = 270
RIGHT = 0
SNAKE_COLOR = '#bfbfbf'
HEAD_COLOR = '#696969'


class Snake():
    def __init__(self):

        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(HEAD_COLOR)


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape='square')
        new_segment.penup()
        new_segment.color(SNAKE_COLOR)
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
    #add a new segment to the snake.
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def reset_position(self):
        for seg in self.segments:
            seg.reset()
            seg.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.head.color(HEAD_COLOR)

