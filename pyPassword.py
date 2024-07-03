import random

print("We are happy to assist secure your life!!!!!!")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x","y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

characters = ["!", "#", "$", "%", "&", "*", "(", ")", "+"]

n_letter = int(input("Enter the number of letter you would like to have in your password: \n"))
n_numbers = int(input("Imput the number of digits you would like to have in your password: \n"))
n_characters = int(input("Enter the number of character s you would like to have in your password: \n"))

#do the letters, practice for loops
letters_pass = ""
for l in range(n_letter):
    letter = random.choice(letters)
    letters_pass += letter

#Do numbers 
numbers_pass = ""
for n in range(n_numbers):
    number = random.choice(numbers)
    numbers_pass += number

#DO characters 
characters_pass = ""
for c in range(n_characters):
    character = random.choice(characters)
    characters_pass += character

final_pass = letters_pass + numbers_pass + characters_pass

print(f'The password save for use is: {final_pass}')
