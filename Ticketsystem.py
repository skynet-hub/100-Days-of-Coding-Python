height = float(input("Enter your height......\n"))
bill = 0

if height >= 120:
    print("You can ride the roller coaster")
    age = int(input("Enter your age: \n"))
    if age < 12:
        bill += 5
        print("Your ride will cose $5")
    elif age >= 12 and age < 18:
        bill += 7
        print("Your ticket costs $7")
    else:
        bill += 12
        print("Your ticket will cost $12")

    photo = input("Do you want to take a photo? enter 'Y' or 'N'\n").lower()
    if photo == "y":
        bill += 3             

else:
    print("You will have to wait to grow taller to ride")

print(f"Your final bill is: {bill}")        