from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

BACKGROUND_COLOR = '#ffd6f8'

screen = Screen()
food = Food()
scoreboard = Scoreboard()

screen.setup(width=600, height=600)
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My snake game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset_score()
        snake.reset_position()


    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_position()


screen.exitonclick()