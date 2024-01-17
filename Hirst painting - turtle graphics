# import colorgram
# Colors = colorgram.extract('hirst-1.jpg',30)
# rgbc = []
# for i in Colors:
#   r = i.rgb.r
#   g = i.rgb.g
#   b = i.rgb.b
#   new_color = (r,g,b)
#   rgbc.append(new_color)
# print(rgbc)
colours_list = [(198, 159, 116), (70, 92, 129), (147, 85, 53), (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93), (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94), (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191), (67, 86, 23), (219, 206, 8)]

import turtle as t
from turtle import Turtle,Screen
import random
tim = Turtle()
tim.hideturtle()
t.colormode(255)
tim.pensize(20)
tim.penup()
tim.goto(-580,-600)
tim.speed("fastest")


s = Screen()


def dots():
    tim.pencolor(random.choice(colours_list))
    tim.dot(20)
    tim.penup()
    tim.forward(50)


def dotrow():
    for i in range(10):
        tim.pencolor(random.choice(colours_list))
        dots()
y=-80
for i in range(10):
    tim.goto(-140,y)
    dotrow()
    y+=50


s.exitonclick()
