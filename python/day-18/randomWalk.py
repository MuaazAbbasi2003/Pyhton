import random
from turtle import Screen, Turtle

val=random.Random()
timmy=Turtle()
def direction2(status):
    match status:
        case 1:
            return timmy.right(val.choice(range(10,100)))
        case 2:
            return timmy.left(val.choice(range(10,100)))
        case 3:
            return timmy.forward(val.choice(range(10,100)))
        case 4:
            return timmy.back(val.choice(range(10,100)))
        case _:
            return "Something's wrong with the Direction"

for x in range(1, 50):
    direction = val.choice([1, 2, 3, 4])
    direction2(direction)


screen=Screen()

screen.exitonclick()