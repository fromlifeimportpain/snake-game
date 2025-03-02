from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(key = "Up", fun = snake.up)
screen.onkey(key = "Down", fun = snake.down)
screen.onkey(key = "Left", fun = snake.left)
screen.onkey(key = "Right", fun = snake.right)

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        score.inc()
        snake.extend()
        
    #Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.ycor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()
        
    #Detect collision with tail.
    for seg in snake.segs[1:]:
        #If head collides with tail, game over.
        if snake.head.distance(seg) < 10:
            score.reset()
    
    

screen.exitonclick()