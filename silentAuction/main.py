import os
from art import logo

print(logo)
bids = {}
bidding_finished = False

def highest_bidder(bidding_records):
    highest_bid = 0
    for bidder in bidding_records:
        bidding_amount = bidding_records[bidder]
        if bidding_amount > highest_bid:
            highest_bid = bidding_amount
            winner = bidder

    print(f"The winner is {winner} at a bid amount of ${highest_bid}")        

while not bidding_finished:

    name = input("Enter your name: ")
    price = eval(input("What is your bid amount: $"))

    bids[name] = price

    should_continue = input("Is there any ther bidder? enter 'yes' or 'no': ").lower()

    if should_continue == 'no':
        bidding_finished = True
        highest_bidder(bidding_records=bids)
    elif should_continue == 'yes':
        os.system('clear')    

