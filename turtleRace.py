from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your Bet", prompt="Which turtle will win the race? Enter a color:  ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-125, -75, -25, 25, 75, 125]

turtle_list = []

for index_turtles in range(0, 6):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index_turtles])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[index_turtles])
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True 

while is_race_on:
    for turtle in turtle_list:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)    

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You have won! The {winning_color} turtle won the race....")
            else:
                print(f"You have lost!, The {winning_color} turtle won the race....")        


screen.exitonclick()
