import turtle
import random

timmy = turtle.Turtle()
colors = ['red', 'blue', 'purple', 'pink', 'brown', 'yellow', 'grey', 'green']

direction = [0, 90, 180, 270]
timmy.pensize(11)
timmy.speed('fast')


for _ in range(200):
   
    color = random.choice(colors)
    timmy.color(color)
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = turtle.Screen()
screen.exitonclick()

