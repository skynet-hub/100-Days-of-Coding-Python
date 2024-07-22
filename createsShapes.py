import turtle

timmy = turtle.Turtle()
start_sides = 3
colors = ['red', 'blue', 'purple', 'pink', 'brown', 'yellow', 'grey', 'green']
start_color = 0

while start_sides < 11:
    timmy.color(colors[start_color])
    for _ in range(start_sides):
        timmy.right(360 / start_sides)
        timmy.forward(65)
    start_sides += 1
    start_color += 1

screen = turtle.Screen()
screen.exitonclick()    