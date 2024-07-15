from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time
screen=Screen()
screen.setup(width=600, height=600)
screen.bgcolor("blue")
screen.title("Welcome to the SNAKE GAME 🐍")
screen.tracer(0) 

score = Score()
snake = Snake()
food = Food()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
#2. MOVING THE SNAKE
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #4. DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()

    #5. DETECT COLLISION WITH WALL
    if snake.head.xcor() > 299 or snake.head.xcor() < -299 or snake.head.ycor() > 299 or snake.head.ycor() < -299:
        game_on = False
        score.over()

    #6.DETECT COLLISION WITH TAIL
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 10:
            game_on=False
            score.over() 

screen.exitonclick() 