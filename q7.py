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


colour = ['green','blue', 'green', 'red', 'pink' ]

for i in range (3,8):
    color( colour[i-3])
    shape(i, i*20)
    penup()
    sety(0)
    setx(xcor() + i*20 + i*30)
    setheading(0)



exitonclick()