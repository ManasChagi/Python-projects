from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

scr = Screen()
scr.setup(height=600, width=800)
scr.bgcolor("black")
scr.title("Ping pong game")
scr.tracer(0)


l_paddle = Paddle(-350,0)
r_paddle = Paddle(350,0)

ball = Ball()
scoreboard = Scoreboard()

scr.listen()
scr.onkey(key="Up", fun=r_paddle.move_up)
scr.onkey(key="Down", fun=r_paddle.move_down)
scr.onkey(key="w", fun=l_paddle.move_up)
scr.onkey(key="s", fun=l_paddle.move_down)

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    scr.update()
    ball.move()

    #detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # if ball misses the r_paddle
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.l_point()

    # if ball misses the l_paddle
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.r_point()


scr.exitonclick()
