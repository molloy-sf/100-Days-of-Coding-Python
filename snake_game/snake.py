from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for coords in STARTING_POSITION:
            new_turtle = Turtle("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.goto(coords)
            self.segments.append(new_turtle)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def snake_up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)

    def snake_down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)

    def snake_left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)

    def snake_right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
