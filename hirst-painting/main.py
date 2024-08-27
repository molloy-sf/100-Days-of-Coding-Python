# import colorgram
#
#
# colors = colorgram.extract('hurst-painting.jpg', 100)
#
# color_list = []
# for x in range(35):
#     color_tuple = ()
#     color = colors[x].rgb
#     color_tuple += color
#     color_list.append(color_tuple)
#
# print(color_list)

import turtle
from turtle import Turtle, Screen
from random import choice


lilt = Turtle()
lilt.shape("turtle")
lilt.color("DarkViolet")
turtle.colormode(255)


def draw_circle(size):
    new_color = choice(color_list)
    lilt.color(new_color)
    lilt.begin_fill()
    lilt.circle(size)
    lilt.end_fill()


def move_forward_nodraw(distance):
    lilt.penup()
    lilt.forward(distance)
    lilt.pendown()


screen = Screen()
color_list = [(244, 242, 237), (228, 234, 241), (245, 237, 241), (235, 243, 238), (214, 157, 85), (33, 105, 151),
              (238, 215, 94), (153, 75, 52), (125, 168, 199), (209, 134, 163), (156, 60, 81), (22, 39, 54),
              (212, 85, 61), (176, 162, 47), (200, 85, 119), (135, 184, 150), (56, 119, 90), (240, 213, 4),
              (25, 46, 37), (228, 167, 186), (64, 46, 34), (87, 157, 100), (9, 99, 75), (34, 166, 189),
              (40, 60, 102), (228, 175, 166), (179, 189, 213), (95, 126, 173), (68, 34, 44), (105, 42, 60),
              (170, 205, 179), (113, 43, 37), (156, 206, 217), (78, 69, 35), (3, 90, 115)]

start_coord_x = -300
start_coord_y = -200
lilt.speed("fastest")

for rows in range(10):
    lilt.teleport(start_coord_x, start_coord_y)
    for columns in range(10):
        draw_circle(20)
        move_forward_nodraw(50)

    start_coord_y += 50

screen.exitonclick()