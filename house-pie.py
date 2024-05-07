# house pie - a square with a triangle roof
import turtle
turtle.shape("turtle") # optional
turtle.speed(1) # optional
turtle.width(4)
#
def square(size):
    for x in range(4):
        turtle.left(90)
        turtle.forward(size)
def triangle(tsize):
    for y in range(3):
        turtle.left(120)
        turtle.forward(tsize)
        
def house(length):
    square(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(270)
    triangle(length)

turtle.color("red")
house(80)
turtle.penup()
turtle.forward(60)
turtle.pendown()
turtle.color("blue")
house(40)
turtle.Screen().exitonclick()

