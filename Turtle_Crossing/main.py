import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()

screen.listen()
screen.onkey(player.move_up,'Up')

car_manager = CarManager()

i = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if i == 5:
        car_manager.create_car()
        i = 0
    i += 1
    car_manager.move()

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        scoreboard.add_level()
        car_manager.speed_up()
        player.position_refresh()

screen.exitonclick()
