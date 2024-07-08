#This program calc number of cans needed to paint a wall
#1 can of paint covers 5 square meters

import math

def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)

    print(f"You will need {number_of_cans} cans to paint this wall")

test_h = int(input("Height of wall: "))  
test_w = int(input("Width of the wall: "))
coverage = 5 

paint_calc(height=test_h, width=test_w, cover=coverage)