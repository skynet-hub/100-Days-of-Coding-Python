import turtle
import random

circ = turtle.Turtle()
turtle.colormode(255)

circ.speed('fastest')

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    color = (r, g, b)
    return color

def draw_circle(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        circ.color(random_color())
        circ.circle(100)
        circ.setheading(circ.heading() + size_of_gap)

draw_circle(5)        

    
   

screen = turtle.Screen()
screen.exitonclick()    
