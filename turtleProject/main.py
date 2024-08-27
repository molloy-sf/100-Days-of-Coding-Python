

# from turtle import Turtle, Screen
#
#
# def move_forward(spaces):
#     timmy.forward(spaces)
#
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("blueviolet")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# move_forward(spaces=100)
#
# my_screen.exitonclick()
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
