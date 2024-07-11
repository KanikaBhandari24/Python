from turtle import Turtle, Screen  #External libraries
tim = Turtle()  #created object
print(tim)
tim.shape("turtle")
tim.color("coral")
tim.forward(100)

screen=Screen()
print(screen.canvheight)
screen.exitonclick()
 
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Charmander"])
table.add_column("Type", ["Electric", "Fire"])
table.align = "l"
print(table)