from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
#1.SCREEN SETUP
screen=Screen()
screen.setup(800, 600)
screen.bgcolor("grey")
screen.title("PONG GAME")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0)) 

ball = Ball()
score=Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #DETECT COLLISION WITH WALL
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #DETECT COLLISION WITH PADDLE
    if ball.distance(r_paddle) < 50 and ball.xcor() >320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #DETECT R PADDLE MISSES
    if ball.xcor() > 380:
        ball.reset()
        score.lpoint()

    #DETECT L PADDLE MISSES
    if ball.xcor() < -380:
        ball.reset()
        score.rpoint()

screen.exitonclick() 