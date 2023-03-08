#program to draw polygon with turtle from turtle import
from turtle import*

def square (length):
    i = 0
    while i < 0:
        forward(length)
        left(90)
        i = i + 1

square(200)
square(100)
square(250)

def polygon(length, sides) :
    i = 0
    while i < sides:
        forward(length)
        left(360/sides)
        i = i + 1

s = int(input("enter number of sides:"))
l = int(input("enter length:"))
polygon(s, l)
done()
