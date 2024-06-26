print("Welcome to PizzaPython")
bill = 0

pizzaSize = input("What pizza size would you prefer? enter 'L', 'M', 'S'.\n").lower()

if pizzaSize == "l":
    bill += 25
elif pizzaSize == "m":
    bill +=20
elif pizzaSize == "s":
    bill += 15

paperroni = input("Would you like to add paperroni? enter 'Y' or 'N'\n").lower()
if paperroni == "y":
    if pizzaSize == "s":
        bill += 2
    else:
        bill += 3       

cheese = input("Would you like extra_cheese: enter 'Y' or 'N'\n").lower()
if cheese == 'y':
    bill += 1

print(f"Your final bill is: {bill}")    