import random
import turtle
from turtle import Screen, Turtle

turtle.colormode(255)
timmy=Turtle()

def forward():
    timmy.forward(100)

def backward():
    timmy.back(100)

screen=Screen()
screen.listen()
screen.onkey(key="w",fun=forward)
screen.onkey(key="s",fun=backward)
screen.exitonclick()
