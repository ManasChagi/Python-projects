from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("brown")
        self.shapesize(stretch_wid=0.5,stretch_len=0.5)
        self.speed("fastest")
        randx = random.randint(-280,280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)


    def refresh(self):
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy)
