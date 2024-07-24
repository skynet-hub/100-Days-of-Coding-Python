# import colorgram

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)    

import turtle
import random

turtle.colormode(255)

color_list = [(144, 76, 50), (188, 165, 117), (248, 244, 246), (166, 153, 36), (14, 46, 85), (139, 185, 176), (146, 56, 81), (42, 110, 136), (59, 120, 99), (145, 170, 177), (87, 35, 30), (64, 152, 169), (220, 209, 93), (110, 37, 31), (100, 145, 111), (165, 99, 131), (91, 122, 172), (158, 138, 158), (177, 104, 82), (55, 52, 85), (206, 182, 195), (68, 48, 63), (73, 51, 71), (173, 201, 194), (175, 198, 201), (213, 182, 176), (37, 47, 45)]


dotty = turtle.Turtle()

def start_pos():
    dotty.hideturtle()
    dotty.penup()
    dotty.goto(-235, -175)


dotty.hideturtle()
start_pos()    

for _ in range(10):

    for _ in range(10):
        dotty.dot(15, random.choice(color_list))
        dotty.forward(50)
    new_cord = dotty.ycor() + 40
    dotty.goto(-235, new_cord)    

screen = turtle.Screen()
screen.exitonclick()

dotty.hideturtle()