from turtle import Turtle, Screen
slow = Turtle()
screen = Screen()
def move():
    slow.forward(20)
#EVENT LISTENER
screen.listen()
screen.onkey(key="space", fun=move)
screen.exitonclick()