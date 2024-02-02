from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over!", align= ALIGNMENT, font=('Courier', 22, 'normal'))



