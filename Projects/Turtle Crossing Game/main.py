import time
from turtle import Screen
from player import Player
from car import Car
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
car=Car()
score=Score()

screen.listen()
screen.onkey(player.up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update() 
    car.create()
    car.move()

    #DETECT COLLISION WITH CAR
    for i in car.cars:
        if i.distance(player) < 20:
            game_on = False
            score.over()

    #DETECT WALL CROSSING
    if player.wall():
        player.start_again()
        car.level() 
        score.increase()

screen.exitonclick() 