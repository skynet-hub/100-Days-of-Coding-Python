from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = randint(1, 6)
        if random_number == 1:
            new_car = Turtle('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(choice(COLORS))
            new_car.penup()
            random_y = randint(-240, 240)
            new_car.goto(300, random_y)   
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def increase_difficulty(self):
        self.car_speed += MOVE_INCREMENT    

    

       
       
     
