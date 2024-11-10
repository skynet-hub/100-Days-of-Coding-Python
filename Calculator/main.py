from art import logo
import os

def add(n1, n2):
    return n1 + n2

def substract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2 

def divide(n1, n2):
        return n1 / n2

operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
} 

def Calculator():

    print(logo)
    try:
        num1 = eval(input("Enter first number: "))
    except NameError:
        print("Invalid input, please enter a number!")
    else:

        for operator in operations:
            print(operator)

        perform_ended = False
        while not perform_ended:
            
            operations_symbol = input("Pick an operation symbol from the list above: ")
            try:
                num2 = eval(input("Enter the next number: "))
            except NameError: 
                print("Invalid input, please enter a number!")
            else:   
                try:        
                    calculation_function = operations[operations_symbol]
                except KeyError:  
                    print("Invalid input, Please enter a valid symbol..")
                else:    
                    if operations_symbol == "/" and num2 == 0:
                        print("Cannot divide with the number 0")
                        break
                    answer = calculation_function(num1, num2)
                    print(f"{num1} {operations_symbol} {num2} = {answer}")

                    goes_on = input(f"Type 'yes' to continue calculating with {answer} or 'no' to start afresh: ").lower()

                    if goes_on == "yes":
                        num1 = answer
                    else:
                        perform_ended =  True
                        os.system("clear")
                        Calculator()

Calculator()               
