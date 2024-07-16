from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.lscore, align="center", font=("Courier", 40, "normal"))
        self.goto(100, 230)
        self.write(self.rscore, align="center", font=("Courier", 40, "normal"))

    def lpoint(self):
        self.lscore += 1
        self.update()

    def rpoint(self):
        self.rscore += 1
        self.update() 