from turtle import Turtle, Screen

sketcher = Turtle()


def move_forward():
    sketcher.forward(10)

def move_back():
    sketcher.back(10)

def counter_clockwise():
    sketcher.left(10)

def clockwise():
    sketcher.right(10)    

def reset():
    sketcher.reset()    


screen = Screen()
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=reset)
screen.exitonclick()