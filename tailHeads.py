#basic program that uses random module to generate heads or tail

import random

print("Welcome to Heads or Tails")

number = random.randint(0, 1)

if number == 0:
    print("Heads")
else:    
    print("Tails")

