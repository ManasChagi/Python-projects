from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.title("Snake Game")
screen.setup(600, 600)
screen.tracer(8)

snake = Snake()
food = Food()
score = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


    #detect collision with food
    if snake.head.distance(food) <= 15:
        food.refresh()
        snake.extend_snake()
        score.increase_score()

    #detect collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280 :
    #     game_is_on = False
    #     score.game_over()

    #detect collision with its own tail (segments)
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()
