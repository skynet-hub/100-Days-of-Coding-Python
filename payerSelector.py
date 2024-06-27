#This program selects a person paying for the meal
import random

print("Welcome to Payer Selector")
print("This program will help you select a random person paying for your meal...")
names = input("Enter the names of people who ate: Seperate names with a comma(,) \n")

list_names = names.split(",")

random_number = random.randint(0, len(list_names)-1)

random_person = list_names[random_number]
print(f"{random_person}, is paying Today!")