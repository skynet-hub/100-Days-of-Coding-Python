from art import logo, vs
from game_data import data
import random
import os

def formatted_data(account):
    """Takes the account data and return the printable format"""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

def check_answer(guess, a_follower, b_follower):
    if a_follower > b_follower:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_continue = True

account_b = random.choice(data)

while game_continue:

    #Generate the random accounts
    account_a = account_b
   
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {formatted_data(account_a)}") 
    print(vs)
    print(f"Against B: {formatted_data(account_b)}")   

    guess = input("Who has more followers? 'A' or 'B': ").lower()

    a_follower = account_a['follower_count']
    b_follower = account_b['follower_count']

    is_correct = check_answer(guess, a_follower, b_follower)

    os.system('clear')
    print(logo)

    if is_correct:
        score += 1
        print(f"You are right!, current score is {score}")
    else:
        game_continue = False
        print(f"Sorry, you are wrong. Final score is {score}")    