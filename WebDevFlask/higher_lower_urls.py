from flask import Flask
from random import randint


#=====Logic part of the game======================
random_num = randint(0, 9)

#==========Flask Application=======================
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" alt"Gif of numbers from 0 to 9">'

#=============Checking user's guess==============
@app.route('/<int:num>')
def guess_check(num):
    if num == random_num:
        return '<h1 style="color:green">You have found me</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif", alt="Pic of a dog going out a tin">'
    elif num > random_num:
        return '<h1 style="color:red">Too high, Try again</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif", alt="Pic of a dog being flan by a human being">'
    else:
        return '<h1 style="color:red">Too low, try again</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif", alt="Pic of a dog digging">'


if __name__ == "__main__":
    app.run(debug=True)