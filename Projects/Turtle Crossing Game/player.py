from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("Black")
        self.goto(0, -280) #OR self.start_again() [the below function]
        self.setheading(90)

    def up(self):
        self.forward(10) 

    def wall(self):
        if self.ycor() > 280:
            return True
        else:
            return False
    
    def start_again(self):
        self.goto(0, -280) 
