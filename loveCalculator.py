print("Welcome to true love calculator!!!")

name1 = input("Enter the name of the first person...\n").lower()
name2 = input("Enter the name of the second person...\n").lower()

combined_name = name1 + name2

T = combined_name.count("t")
R = combined_name.count("r")
U = combined_name.count("u")
E = combined_name.count("e")

L = combined_name.count("l")
O = combined_name.count("o")
V = combined_name.count("v")
E = combined_name.count("e")

true = str(T + R + U + E)
love = str(L + O + V + E)

final_count = true + love
int_count = int(final_count)

if int_count < 10 or int_count > 90:
    print(f"Your score is: {int_count}, you go together like coke and mentos!!")
elif int_count <= 40 or int_count >= 50:
    print(f"Your score is {int_count}, you are alright together..")
else:
    print(f"Your score is: {int_count}")        
