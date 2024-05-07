# stop signs
import turtle
turtle.shape("turtle") # optional
turtle.speed(1) # optional
turtle.width(3)
def rectangle(sizet):
    turtle.right(90)
    turtle.forward(sizet)
    turtle.left(90)
    turtle.forward(sizet/10)
    turtle.left(90)
    turtle.forward(sizet)


def octagon(sizeo):
    turtle.right(90)
    turtle.forward(sizeo * (3/8))
    for i in range(8):
        turtle.left(45)
        if i == 8:
            turtle.forward(sizeo * (3/8))
        else:
            turtle.forward(sizeo)

turtle.color("red")
rectangle(90)
octagon(60)
turtle.penup()
turtle.forward(170)
turtle.color("blue")
turtle.pendown()
rectangle(150)
octagon(90)
turtle.Screen().exitonclick()