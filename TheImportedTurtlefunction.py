#TheImportedTurtlefunction
import turtle
turtle.shape("turtle") # optional
turtle.speed(1) # optional
turtle.width(4)
#
def draw_me_a_():
    for side in range(4):
        for steps in range(10):
            for c in ('blue', 'red', 'green', 'purple'):
                turtle.color(c)
                turtle.forward(steps)
        turtle.left(90)
#
def step_aside():
    turtle.penup()
    turtle.right(180)
    turtle.forward(180)
    turtle.right(90)
    turtle.forward(10)
    turtle.pendown()

draw_me_a_()
step_aside()
draw_me_a_()
turtle.Screen().exitonclick()
