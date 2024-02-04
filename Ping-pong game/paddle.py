from turtle import Turtle,Screen
scr = Screen()

class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(x=x, y=y)
    def move_up(self):
        newy = self.ycor()+25
        self.goto(self.xcor(),newy)
    def move_down(self):
        newy = self.ycor() - 25
        self.goto(self.xcor(), newy)

