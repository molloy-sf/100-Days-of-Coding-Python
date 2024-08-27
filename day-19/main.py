from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter a color: ")
print(f"User bets on {user_bet}.\n")
colors = ["red", "blue", "orange", "yellow", "green", "purple"]

turtle_shape = "turtle"
count = len(colors)
start_line = -230
finish_line = 220
bottom = -100
all_turtles = []

# Make 6 turtles, one per color
for x in range(count):
    turtle = Turtle(shape=turtle_shape)
    turtle.penup()
    turtle.color(colors[x])
    turtle.goto(x=start_line, y=bottom + (x * 40))
    all_turtles.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        rand_dist = randint(0, 10)
        turtle.forward(rand_dist)
        if turtle.xcor() >= finish_line:
            winner = turtle.pencolor()
            is_race_on = False
            if winner == user_bet:
                print(f"You won! The {winner} turtle won the race!")
            else:
                print(f"You lost. The {winner} turtle won the race.")

# screen.exitonclick()
