from turtle import *

speed(10)
penup()
setpos(-650,0)

def shape(sides, size):
    for i in range((sides*5)-1):
        pendown()
        fd(size)
        left(360/sides)
        penup()
        size -= 10/sides


    
for i in range (3,6):
    shape(i, i*20)
    penup()
    newx = pos() + i*20
    setpos(newx , 0)
    setheading(0)

exitonclick()