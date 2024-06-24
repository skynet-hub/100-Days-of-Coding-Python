print("Welcome to tip Calculator!!")

#Get user inputs

bill = float(input("Enter the amount of the bill: \n"))
tip = float(input("Provide the tip you would like to give? 10 12 or 15.\n"))
people = int(input("Enter the number of people you want to split the bill among? \n"))

#compute calculations

total_bill = bill * (1 + (tip / 100))
split_bill = total_bill / people

final_amout = "{:.2f}".format(split_bill)

#printout the results

print(f"Each and ever one will pay {final_amout}")

