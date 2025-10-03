from turtle import *

penup()
setpos(-300,-300)


def shape(sides, size):
    for i in range(sides):
        pendown()
        fd(size)
        left(360/sides)
        penup()
        


colour = ['green','blue', 'green', 'red', 'pink' ]


for i in range(3,7):
    color(colour[i-3])
    shape(i,20*i)
    penup()
    forward(30*i + 60)



exitonclick()