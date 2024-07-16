from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
    #1.CREATE PADDLE
        self.shape("square")
        self.color("black")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    #2.MOVE self
    def up(self):
        newy = self.ycor() + 20
        self.goto(self.xcor(), newy)
    def down(self):
        newy = self.ycor() - 20
        self.goto(self.xcor(), newy) 