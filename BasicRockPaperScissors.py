import random

#Rock paper and scissiors v1

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("Welcome to rock, paper and scissors, hope it helps ou reach a conclusion, Enjoy!!!!")

player1_choice = int(input("What do you choose? 0 for rock, 1 for paper and 2 for scissors: \n"))

#make the computer decision part of the game

computer_choice = random.randint(0, 2)

arts = [rock, paper, scissors]

#make print statements to showcase player choices and their hand signs
if player1_choice >= 3 or player1_choice < 0:
    print("You chose an invalid operation, You lose!")
else:
    print(arts[player1_choice])
    print("Computer chose: ")
    print(arts[computer_choice])

    #Now into the logic of the game, determining the winner or loser
    if computer_choice == 2 and player1_choice == 0:
        print("You win!")
    elif player1_choice == 2 and computer_choice == 0:
        print("You lose!")    
    elif computer_choice > player1_choice:
        print("You Lose")
    elif player1_choice > computer_choice:
        print("You win")        
    elif player1_choice == computer_choice:
        print("it is a draw, run again to determine winner!")    
            


