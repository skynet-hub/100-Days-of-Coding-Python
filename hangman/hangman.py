import random 

RED = "\u001B[31m"
GREEN = "\u001B[32m"
RESET = "\u001B[0m"

from arts import logo, stages

from words import word_list
chosen_word = random.choice(word_list)

#replace all the letters in the chosen word with blanks

display = []
for _ in range(len(chosen_word)):
    display += "_"

print(display)    

#create repeatability
end_game = False
lives = 6

while not end_game:

    guess = input("Choose a word....: ").lower()

    #where user guesses right replate place with the letter they guessed
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = letter

    print(display)        

    if guess not in chosen_word:
        lives -= 1
        print("Incorrect, you lose a life")
        if lives == 0:
            print(f"You have {lives} lives remaining, Game over!!")
            print(f"{RED}The correct word was {chosen_word}")
            end_game = True

    if "_" not in display:
        print(f"{GREEN}You have successfully guesse all the letters in the word, You win!!!!") 
        end_game = True               

    print(stages[lives])