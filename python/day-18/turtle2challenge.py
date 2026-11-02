import random
import turtle
from turtle import Screen, Turtle

turtle.colormode(255)
timmy=Turtle()
def randomcolor():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    color=(r,g,b)
    return color

timmy.speed("fastest")
timmy.penup()
timmy.goto(-300, 300)
timmy.setheading(0)
timmy.pendown()

for i in range(10):
    for x in range(10):
        timmy.pendown()
        timmy.circle(10)

        timmy.penup()
        timmy.forward(40)

    # Move to the start of the next row
    timmy.goto(-300, timmy.ycor() - 60)
    timmy.setheading(0)



screen=Screen()

screen.exitonclick()

