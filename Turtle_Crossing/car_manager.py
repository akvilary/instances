from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COR = 300
Y_COR_LIST = []
Y_COR = 250
for y in range(8):
    Y_COR_LIST.append(Y_COR)
    Y_COR -= 65

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.car_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.hideturtle()
        self.last_y = 0
        self.all_cars = []

    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.color(random.choice(COLORS))
        new_car.shape('square')
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.x_cor = X_COR
        new_car.y_cor = random.choice(Y_COR_LIST)
        while new_car.y_cor == self.last_y:
            new_car.y_cor = random.choice(Y_COR_LIST)
        self.last_y = new_car.y_cor
        new_car.goto(new_car.x_cor,new_car.y_cor)
        self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT

