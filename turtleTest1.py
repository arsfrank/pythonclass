from turtle import *

color("red", "yellow")
pensize(5)
i = 0
sides = 5
while i < sides:
    forward(100)
    left(360/sides)
    i = i + 1
done()
