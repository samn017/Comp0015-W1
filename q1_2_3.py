from turtle import *

penup()
setpos(-200,-200)

def square(x):
    for i in range(4):
        pendown()
        forward(x)
        left(90)
        penup()

y=1
while y != 5:
    for c in ('green','blue','green','red'):
        color(c)
        square(20*y)
        penup()
        forward(20*y+10)
        y += 1



exitonclick()
