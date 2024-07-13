#REFER TO TURTLE DOCUMENTATION
from turtle import Turtle, Screen
import random
slow = Turtle()
slow.shape("turtle")
slow.color("blue")
slow.forward(100)
slow.left(90)
screen = Screen()
screen.exitonclick()

# CHALLENGE 1 - TURTLE SQUARE
slow = Turtle()
slow.shape("turtle")
slow.color("blue")
slow.forward(100)
slow.right(90)
slow.forward(100)
slow.right(90)
slow.forward(100)
slow.right(90)
slow.forward(100)
# OR USING FOR LOOP
for i in range(4):
    slow.forward(100)
    slow.right(90)  
screen = Screen()
screen.exitonclick() 

# CHALLENGE 2 - DRAW A DASHED LINE
slow = Turtle()
slow.shape("turtle")
slow.color("blue") 
slow.forward(20)
slow.penup()
slow.forward(20)
slow.pendown()
slow.forward(20)    
slow.penup()
slow.forward(20)
slow.pendown()
slow.forward(20)
for i in range(4):
    slow.forward(20)
    slow.penup()
    slow.forward(20)
    slow.pendown()
screen = Screen()
screen.exitonclick() 

#CHALLENGE 3 - DRAW DIFFERENT SHAPES
slow = Turtle()
slow.shape("turtle")
slow.color("blue") 
color=["wheat","LightSeaGreen","SeaGreen","DeepSkyBlue","DarkOrchid"]
def shape(sides):
    angle = 360/sides
    for i in range(sides):
        slow.forward(100)
        slow.right(angle)
for n in range(3, 11):
    slow.color(random.choice(color))
    shape(n)
screen = Screen() 
screen.exitonclick() 

#CHALLENGE 4 - RANDOM WALK
slow = Turtle()
slow.shape("turtle")
slow.color("blue") 
color=["wheat","LightSeaGreen","SeaGreen","DeepSkyBlue","DarkOrchid"]
direction = [0, 90, 180, 270]
for i in range(100):
    slow.color(random.choice(color))
    slow.forward(20)
    slow.setheading(random.choice(direction))
screen = Screen()
screen.exitonclick() 

#CHALLENGE 5 - MAKING A SPIROGRAPH
slow = Turtle()
slow.shape("turtle")
slow.color(255)
def random_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    color = (r,g,b)
    return color
slow.speed("fastest")

for i in range(100):
    slow.color(random_color())
    slow.circle(100)
    slow.setheading(slow.heading() + 10)
screen = Screen()
screen.exitonclick()
