import turtle
import random

timmy = turtle.Turtle()
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    random_color = (r, g, b)
    return random_color

direction = [0, 90, 180, 270]
timmy.pensize(11)
timmy.speed('fast')


for _ in range(200):
   
    timmy.color(random_color())
    timmy.forward(30)
    timmy.setheading(random.choice(direction))


screen = turtle.Screen()
screen.exitonclick()

