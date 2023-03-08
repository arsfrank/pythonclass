from turtle import *

i = 1
pensize(5)
color("red", "yellow")
begin_fill()
while True:
    forward(200)
    left(135)
    if abs(pos()) < 1:
        break
end_fill()

penup()
goto(-200, -100)
pendown()
color("blue", "teal")
begin_fill()
circle(100)
end_fill()
done()



