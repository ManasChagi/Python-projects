from turtle import Turtle
FONT = ('Courier', 20, 'normal')
ALIGNMENT = 'center'
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as d:
            self.highscore = int(d.read())
        self.penup()
        self.goto(0, 265)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High Score = {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as d:
                d.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()
