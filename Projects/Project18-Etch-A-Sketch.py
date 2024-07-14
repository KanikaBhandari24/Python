from turtle import Turtle, Screen
slow = Turtle()
screen = Screen()
def move_forward():
    slow.forward(50)

def move_backward():
    slow.backward(30)

def move_left():
    new = slow.heading() + 40
    slow.setheading(new)
    # OR slow.left(10)

def move_right():
    slow.right(30)

def clear():
    slow.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")
screen.exitonclick() 