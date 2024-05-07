import turtle
turtle.shape("turtle") # optional
turtle.speed(1) # optional
turtle.width(4)
#
#square1
for side in range(4):
    for steps in range(10):
        for c in ('blue', 'red', 'green', 'purple'):
            turtle.color(c)
            turtle.forward(steps)
    turtle.left(90)
#
#step aside
turtle.penup()
turtle.left(180)
turtle.forward(180)
turtle.pendown()
#
#square2
for side in range(4):
    for steps in range(10):
        for c in ('purple', 'green', 'red', 'blue'):
            turtle.color(c)
            turtle.forward(steps)
    turtle.right(90)
turtle.Screen().exitonclick()
