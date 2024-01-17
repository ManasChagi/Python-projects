
import random
import turtle
from turtle import Turtle, Screen
screen = Screen()

def all_colors():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r, g, b)
    return color


tim = Turtle()
# tim.shape("turtle")
tim.color("DarkSeaGreen4")
# tim.pensize(15)
# dir = [0,90,270,180,360]
turtle.colormode(255)

tim.speed("fastest")
def spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(all_colors())
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)

spirograph(1)
# for i in range(300):
#     tim.color(all_colors())
#     tim.forward(30)
#     tim.setheading(random.choice(dir))
#

screen.exitonclick()


