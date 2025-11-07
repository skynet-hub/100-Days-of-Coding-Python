#############My BlackJack rules###############
#The deck is unlimited in size
#There are no Jokers
#The Jack/Queen/King all cout as 10
#The ace can count as 11 or 1
#The cards in the list have equal probability of being drawn
#Cards are not removed from the deck as they are drawn

#Here's the list of cards

import random
from art import logo
import os

def blackjack():
      
    print(logo)
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def deal_card():
        """Returns a random card from the deck"""
        return random.choice(cards)

    def calculate_score(cards):
        """Takes in a list of cards and return a score of these cards"""                       

        if sum(cards) == 21 and len(cards) == 2:
            return 0 #This represents a blackjack in our game

        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)  

        return sum(cards)    


    def compare(u_score, c_score):
        if u_score == c_score:
            return f"user's score is {u_score} and computer's score is {c_score}, it is a draw!"
        elif c_score == 0:
            return "The computer has a black jack you lose!"
        elif u_score == 0:
            return "You have a blackJack you win!!"
        elif c_score > 21:
            return "The computer has went over, You win!!!"
        elif u_score > 21:
            return "You have went over, you lose!!!"
        else:
            if u_score > c_score:
                return "You have scored higher, You win"
            elif c_score > u_score:
                return "You have scored lower, you lose!!!!"    

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")   

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            another_card = input("would you like another card: 'yes' or 'no' ").lower()
            if another_card == 'yes':
                user_cards.append(deal_card())
            else:
                is_game_over = True    

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)     
      
    print(compare(u_score=user_score, c_score=computer_score))
    print(f"Computer's hand is {computer_cards}, final score is: {computer_score}")



    another_round = input("Do you want to play a game of blackjack? 'yes' or 'no': ").lower()
    while another_round == True:
        os.system('clear')
        blackjack()

blackjack()          