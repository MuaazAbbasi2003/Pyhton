import random
import turtle
from turtle import Screen, Turtle

colors=["Red","Yellow","Blue","Green","Purple"]
x=-300
y=-200
for col in colors:
    val= Turtle(shape="turtle",)
    val.penup()
    val.goto(x,y)
    val.color(col)
    y +=100


screen=Screen()
screen.exitonclick()