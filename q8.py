from turtle import *

speed(10)
penup()
setpos(-650,0)

def star(points, size):
    for i in range(points):
        x = round(points/2 -1, 0)
        pendown()
        fd(size)
        right(360/points * x)
        

colour = ['green','blue', 'green', 'red', 'pink' ]

for i in range (8,13):
    color(colour[i-8])
    star(i,50)
    penup()
    sety(0)
    setx(xcor()+70)

exitonclick()