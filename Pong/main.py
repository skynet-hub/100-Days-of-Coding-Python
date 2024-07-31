from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title('PONG')
screen.bgcolor('black')
screen.tracer(0)

right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))


screen.listen()
screen.onkey(key='Up', fun=right_pad.go_up)
screen.onkey(key='Down', fun=right_pad.go_down)
screen.onkey(key = "w", fun =left_pad.go_up)
screen.onkey(key="s", fun=left_pad.go_down)

ball = Ball() 
score = ScoreBoard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.moving_speed)
    ball.move_ball()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()   

    if ball.distance(right_pad) < 50 and ball.xcor() > 320 or ball.distance(left_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()     

    if ball.xcor() > 380:
        ball.reset_position()
        score.increase_l()

    if ball.xcor() < -380:
        ball.reset_position()
        score.increase_r()
           
screen.exitonclick()