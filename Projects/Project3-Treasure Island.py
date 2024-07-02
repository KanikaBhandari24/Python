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
print("*************** Welcome to Treasure Island. ***************\n")
print("Your mission is to find the treasure.\n") 

print("You are at a crossroad. Where you want to go?\n")
direction=input("Type 'Left' or 'Right'?\n")
if direction=='Left':
          print("You came to a lake. There is an island in the middle of the lake!\n")
          activity=input("Type 'Swim' or 'Wait'\n")
          if 'Wait':
                    print("You arrived at the island. There are three doors, which door you want to choose?\n")
                    color=input("Type 'Red', 'Blue' or 'Yellow'?\n")
                    if color=='Red':
                              print("Burned by fire! Game over...")
                    elif color=='Blue':
                              print("Eaten by Beasts! Game Over...")
                    elif color=='Yellow':
                              print("YOU WON THE GAME")
                    else:
                              print("Game over...")
          else:
                    print("Attacked by trout! Game over...")
else:
    print("Oops you fall into a hall!\nGame Over...")
