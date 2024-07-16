from turtle import Turtle
FONT = ("Arial", 24, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup() 
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", align="left", font="FONT")

    def increase(self):
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align="left", font="FONT")

    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font="FONT")

