from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.cars=[]
        self.speed = STARTING_MOVE_DISTANCE

    def create(self):
        choice = random.randint(1, 6)
        if choice == 1:
            car=Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(COLORS))
            randomy=random.randint(-250, 250)
            car.goto(300, randomy)
            self.cars.append(car)
    
    def move(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level(self):
        self.speed += MOVE_INCREMENT
