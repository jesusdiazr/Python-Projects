from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

y = -100
for colour in range(len(colors)):
    turtles.append(Turtle(shape="turtle"))
    turtles[colour].color(colors[colour])
    turtles[colour].penup()
    turtles[colour].goto(x=-230, y=y)
    y += 40

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() >= 230:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You've won! The winning color is {winner}!")
            else:
                print(f"You've lost! The winning color is {winner}!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()
