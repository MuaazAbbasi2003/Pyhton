import random
from turtle import Screen, Turtle

random1=random.Random()
timmy=Turtle()
timmy.shape("turtle")
timmy.color("Green")
shapes=[3,4,5,6,7,8,9,10]
random_colors = [
    "#E63946", "#F1FAEE", "#A8DADC", "#457B9D", "#1D3557",
    "#FFB703", "#FB8500", "#023047", "#8ECAE6", "#219EBC",
    "#6A4C93", "#1982C4", "#8AC926", "#FFCA3A", "#FF595E",
    "#2EC4B6", "#FF9F1C", "#E71D36", "#011627", "#FDFFFC",
]
val=360
forward= 50
for shape in shapes:
    angle = val / shape
    for x in range(shape):
        timmy.pencolor(random1.choice(random_colors))
        timmy.forward(forward)
        timmy.right(angle)

screen=Screen()

screen.exitonclick()