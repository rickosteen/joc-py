#Square_to_Rectangle_funct
#TheImportedTurtlefunction
import turtle
turtle.shape("turtle") # optional
turtle.speed(1) # optional
turtle.width(4)
#
def anyshape(sides, leng, ang, rect):
    for x in range(sides):
        if rect == "y":
            turtle.left(ang)
            turtle.forward(leng *2)
            turtle.left(ang)
            turtle.forward(leng)
        else:
            turtle.left(ang)
            turtle.forward(leng)
#
anyshape(4, 30, 90, "y")
