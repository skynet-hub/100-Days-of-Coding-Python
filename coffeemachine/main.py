
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

def check_resources(resources):
    answer = 0
    ingredients = MENU[user_want]['ingredients']
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there's is not enough {ingredient}")
            answer += 1

    return answer      

def process_coins():
    quaters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: ")) 
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))

    total = (quaters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01) 
    return total   

def transaction_successful(money_received, resources):
    cost = MENU[user_want]['cost']
    if cost > money_received:
        print("Sorry that is not enough money, Money refunded!!")
    else:
        change = round(money_received - cost, 2)
        print(f"Here's ${change} in change")
        resources['money'] += cost
        return False
        
def make_coffee(resources):
    ingredients = MENU[user_want]['ingredients']

    for ingredient in ingredients:
        for resource in resources:
            if ingredient == resource:
                resources[resource] -= ingredients[ingredient]

    print(f"Here's your {user_want}, Enjoy!!!")
        

machine_on = True
while machine_on:
    user_want = input("What would you like? (espresso/latte/cuppaccino): ").lower()

    if user_want == 'off':
        machine_on = False
    elif user_want == 'report':
        for resource in resources:
            print(f"{resource}: {resources[resource]}")
    else:
         if check_resources(resources) == 0:
            money_received = process_coins()
            if transaction_successful(money_received, resources) == False:
                make_coffee(resources)
              
       
        