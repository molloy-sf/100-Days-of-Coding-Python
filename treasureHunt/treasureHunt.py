print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
print("")
first_decision = input(
    "You have come to a fork in the road. To the left, you see more of the same indistinct landscape you have encountered thus far. To the right, you see a slight hill but nothing else beyond. Which way will you go? (Enter Left or Right) ")
if first_decision.lower() == "left":
    print("")
    second_decision = input(
        "After walking a short distance down this path, you come to a wide but gently flowing river. You see a small island in the middle of the river with a boat docked on the shore. You can either wait for the boat to take you to the island or you can swim the short distance to the island. Which will you do? (Enter Swim or Wait) ")
    if second_decision.lower() == "wait":
        print("")
        third_decision = input(
            "After waiting only a few minutes for the boat to magically float itself across the river to you, you hop in and ride out to the small island where you see a house with 3 doors. One door is red, one is blue and one is yellow. Which door will you open? (Enter Red, Blue or Yellow) ")
        if third_decision.lower() == "yellow":
            print("")
            print("You open the Yellow door and find a room full of gold and jewels. You found the treasure!")
        elif third_decision.lower() == "red":
            print("")
            print(
                "You open the Red door and are immediately sucked into the maw of a dragon moments before it breathes out its fiery breath and burns you to a crisp. Game Over.")
        elif third_decision.lower() == "blue":
            print("")
            print(
                "You open the Blue door only to find you have been instantly teleported to the cold wastes of the south pole. Game Over.")
        else:
            print("")
            print("Your lack of comprehension has finally spelled your doom! Game Over.")

    else:
        print("")
        print(
            "You decide to swim the short distance to the island. As you swim, you feel something brush against your leg. You look down and see a large trout. You try to swim back to the shore but the trout is too fast and you are eaten up. Game Over.")

else:
    print("")
    print(
        "You walk up the small hill only to find the road beyond has crumbled away into an abyss below. While gazing into the abyss, you feel a strange pull. before thinking about it you jump off the edge.... Game Over.")
