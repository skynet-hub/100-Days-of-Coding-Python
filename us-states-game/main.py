import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

def update_state(turtle, x, y):
    turtle.home()
    turtle.goto(x, y)
    turtle.write(name_state)
    

FONT = ('courier', 11, 'normal')

score = 0
correct_state = []

while score < 50:

    user_input = screen.textinput(title=f"{score}/50 State correct", prompt="What is another state's name: ").title()

    states_data = pandas.read_csv("./50_states.csv")

    if user_input == "Exit":
        missing_state = [state for state in states_data.state if state not in correct_state]
        df = pandas.DataFrame(missing_state)
        df.to_csv("./missing_states.csv")     
        break

    for state in states_data.state:
        if user_input == state:
            state_row = states_data[states_data.state == state]
            x_coor = state_row["x"].squeeze()
            y_coor = state_row["y"].squeeze()
            name_state = state_row["state"].squeeze()
            staty = turtle.Turtle()
            staty.penup()
            staty.hideturtle()
            update_state(staty, x_coor, y_coor)
            score += 1
            correct_state.append(name_state)


