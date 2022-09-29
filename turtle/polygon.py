import turtle

#this function creates an n sided regular polygon
def polygon(sides):
    angle = 360/sides
    for i in range(sides):
        turtle.forward(100)
        turtle.right(angle)
    turtle.done()
