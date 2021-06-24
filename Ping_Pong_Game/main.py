from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('#000000')
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

first_player = Paddle('left')
fp_score = Scoreboard((50, 250))
second_player = Paddle('right')
sp_score = Scoreboard((-50, 250))
ball = Ball()

screen.listen()
screen.onkey(fun=first_player.up, key='w')
screen.onkey(fun=first_player.down, key='s')
screen.onkey(fun=second_player.up, key='Up')
screen.onkey(fun=second_player.down, key='Down')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    #Detecting collision with the paddle
    if ball.xcor() > 320 and second_player.distance(ball) < 50:
                #needs to bounce
                ball.bounce_x()

    elif ball.xcor() < -320 and first_player.distance(ball) < 50:
            #needs to bounce
            ball.bounce_x()

    if ball.xcor() > 380:
        fp_score.add_score()
        ball.reset_position()

    elif ball.xcor() < -380:
        sp_score.add_score()
        ball.reset_position()
    #
    #Detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #needs to bounce
        ball.bounce_y()




















screen.exitonclick()