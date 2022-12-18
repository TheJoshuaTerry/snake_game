from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.listen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Welcome to Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

screen.update()
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        score_board.draw_line()
        snake.extend()


    # Detect Collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 270 or snake.head.ycor() < -280:
        score_board.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()


screen.exitonclick()