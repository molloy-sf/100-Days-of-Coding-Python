import turtle
from turtle import Turtle, Screen
from random import choice, randint

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("DarkViolet")
turtle.colormode(255)

def move_forward_draw(distance):
    timmy_the_turtle.speed(7)
    timmy_the_turtle.pensize(5)
    timmy_the_turtle.pendown()
    timmy_the_turtle.forward(distance)
    timmy_the_turtle.penup()


def move_forward_nodraw(distance):
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(distance)
    timmy_the_turtle.pendown()


def turn_right(angle):
    timmy_the_turtle.right(angle)


def randcolor():
    # randnum = choice(["red", "blue", "orange", "yellow", "green", "purple", "brown", "maroon", "violet", "grey"])
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    new_color = (r, g, b)
    print(new_color)
    return new_color


def randdirection():
    rd = (choice([0, 1, 2, 3]) * 90)
    print(rd)
    return rd


# Draw a square
# for x in range(4):
#     move_forward(100)
#     turn_right(90)

# Draw a dashed line
# timmy_the_turtle.teleport(-200)
# for x in range(15):
#     move_forward_draw(10)
#     move_forward_nodraw(10)

# for x in range(3, 11):
#     timmy_the_turtle.pencolor(randcolor())
#     for sides in range(x):
#         move_forward_draw(100)
#         turn_right(360 / x)

# for x in range(10, 50):
#     timmy_the_turtle.pencolor(randcolor())
#     move_forward_draw(20)
#     timmy_the_turtle.setheading(randdirection())

timmy_the_turtle.speed("fastest")
for x in range(73):
    timmy_the_turtle.pencolor(randcolor())
    timmy_the_turtle.circle(100)
    timmy_the_turtle.left(5)












screen = Screen()
screen.exitonclick()