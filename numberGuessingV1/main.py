import random
from art import logo

print(logo)
print("Welcome to the number Guessing game.....")
print("Guess a number between '1' and '100':")

chosen_number = random.randint(1, 100)
lives = 10

def easy():
    global lives

    print(f"You have {lives} remaining....")

    game_on = True
    while game_on:
        guess = int(input("Make a guess: "))

        if guess == chosen_number:
            game_on = False
            print(f"You got it, the number is {guess}....")
        elif guess > chosen_number:
            lives -= 1
            print(f"The number {guess}, is greater than the chosen number...")
            print(f"You have {lives} lives remaining")
        elif guess < chosen_number:
            lives -= 1
            print(f"The number {guess}, is less than the chosen number...")
            print(f"You have {lives} lives remaining")   
        else:
            lives -= 1
            print(f"You have entered an invalid option {guess}")
            print(f"You have {lives} remaining")   

        if lives == 0:
            game_on = False
            print("Game over")     

def hard():
    global lives
    lives //= 2
    print(f"You have {lives} remaining....")

    game_on = True
    while game_on:
        guess = int(input("Make a guess: "))

        if guess == chosen_number:
            game_on = False
            print(f"You got it, the number is {guess}....")
        elif guess > chosen_number:
            lives -= 1
            print(f"The number {guess}, is greater than the chosen number...")
            print(f"You have {lives} lives remaining")
        elif guess < chosen_number:
            lives -= 1
            print(f"The number {guess}, is less than the chosen number...")
            print(f"You have {lives} lives remaining")   
        else:
            lives -= 1
            print(f"You have entered an invalid option {guess}")
            print(f"You have {lives} remaining")   

        if lives == 0:
            game_on = False
            print("Game over")                   

level = input("Do you want to play the 'easy' or 'hard' level: ").lower()
if level == "easy":
    easy()
elif level == "hard":
    hard()    