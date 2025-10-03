from turtle import *

speed(50)
penup()
setpos(-650,0)

def shape(sides, size):
    for i in range(sides):
        pendown()
        fd(size)
        left(360/sides)
        penup()
        


colour = ['green','blue', 'green', 'red', 'pink' ]


for x in range (3,6):
    color(colour[x-3])
    for i in range (10):
        shape(x, x*20)
        penup()
        left(36)
    
    forward(i*30+50)



exitonclick()


        
