from turtle import Turtle, Screen
import random
screen=Screen()
race = False
screen.setup(width=500, height=500)
user = screen.textinput(title="Turtle race", prompt="Which color turtle you choose?")
color=["red","orange","yellow","blue"]
position=[-80, -20, 40, 100]
turtles=[]
for index in range(0, 4):
    slow = Turtle(shape="turtle")
    slow.color(color[index])
    slow.penup()
    slow.goto(x=-230, y=position[index])
    turtles.append(slow)
if user:
    race = True

while race:
    for turtle in turtles:
        if turtle.xcor()>230:
            race = False
            win = turtle.pencolor()
            if win == user:
                print(f"You have won! The {win} is the winner.")
            else:
                print(f"You have lost. The {win} turtle is the winner.")
        dist = random.randint(0, 10)
        turtle.forward(dist)
screen.exitonclick()  