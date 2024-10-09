from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# Screen configuration
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        score.refresh_score()
        food.refresh()














screen.exitonclick()