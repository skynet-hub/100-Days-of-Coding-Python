#This program selects a person paying for the meal
import random

print("Welcome to Payer Selector")
print("This program will help you select a random person paying for your meal...")
names = input("Enter the names of people who ate: Seperate names with a comma(,) \n")

list_names = names.split(",")

random_person = random.choice(list_names)

print(f"{random_person}, is paying Today!")