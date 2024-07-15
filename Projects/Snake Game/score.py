from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.write(f"Your Score: {self.score}", False, "center", ("Arial", 14, "normal"))
        self.hideturtle()
    
    def over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", ("Arial", 14, "normal"))
    
    def increase(self):
        self.score += 1
        self.clear() 
        self.write(f"Your Score: {self.score}", False, "center", ("Arial", 14, "normal"))
 