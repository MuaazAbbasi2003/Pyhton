from turtle import Screen, Turtle

from prettytable import PrettyTable

timmy= Turtle()
myScreen=Screen()
print(myScreen.canvheight)
myScreen.exitonclick()
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charizad"])

print(table)