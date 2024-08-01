import turtle
import time
import snake
from food import Food
from scoreboard import ScoreBoard

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("My Snake Game")
screen.bgcolor(0, 0, 0)
screen.tracer(0)

my_snake = snake.Snake()
food = Food()
score = ScoreBoard()



screen.listen()
screen.onkey(key="Up", fun=my_snake.up)
screen.onkey(key="Down", fun=my_snake.down)
screen.onkey(key="Right", fun=my_snake.right)
screen.onkey(key="Left", fun=my_snake.left)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    my_snake.move()

    #detect collision
    if my_snake.head.distance(food) < 15:
        my_snake.extend_segment()
        score.increase_score()
        food.reshuffle()

   
    if my_snake.head.xcor() > 280 or my_snake.head.xcor() < -280 or my_snake.head.ycor() > 280 or my_snake.head.ycor() < -280:
        score.reset_scoreboard()
        my_snake.reset_snake()

    #detect collision with body
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment) < 5:
            score.reset_scoreboard() 
            my_snake.reset_snake()
        












screen.exitonclick()




