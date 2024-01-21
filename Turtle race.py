from turtle import Turtle, Screen
screen = Screen()
screen.setup(height=400, width=500)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors =["red","gold","blue","green","purple","orange"]
z =[100,70,40,10,-20,-50,-80]
allt = []
for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.goto(x=-230, y=z[i])
    allt.append(tim)

if user_bet:
    is_race_on = True
import random
while is_race_on:
    for turtle in allt:
        rand_dist = random.randint(0,10)
        turtle.forward(rand_dist)
        if turtle.xcor()>230:
            is_race_on = False
            win = turtle.pencolor()
            if user_bet == win:
                print(f"Congo! you've won!!, the winning color is {win}")
            else:
                print(f"You've lost {win} turtle is the winner, try again next time!")


screen.exitonclick()
