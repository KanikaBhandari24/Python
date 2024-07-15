from turtle import Turtle
POSITIONS=[(0, 0), (-20, 0), (-40, 0)]
MOVE=20
UP=90
DOWN=270
LEFT=180
RIGHT=0
class Snake:
    def __init__(self):
        self.segment=[]
        self.create()
        self.head=self.segment[0]

    def create(self):
        # WILL CREATE A SNAKE BODY 
        # slow = Turtle("square")
        # slow.color("yellow")
        # slow1 = Turtle("square")
        # slow1.color("yellow")
        # slow1.goto(-20,0)
        # slow2 = Turtle("square")
        # slow2.color("yellow")
        # slow2.goto(-40,0)

        for i in POSITIONS:
            self.add(i) 

    def add(self, position):
        slow = Turtle(shape="square")
        slow.color("yellow")
        slow.penup()
        slow.goto(position)
        self.segment.append(slow)
    
    def extend(self):
        #INCREASE THE SNAKE BODY EVERYTIME IT EATS FOOD
        self.add(self.segment[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)



    def move(self):
        for seg in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.head.forward(MOVE)
