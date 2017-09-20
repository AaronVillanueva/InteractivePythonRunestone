import turtle
turtle.color("blue")
turtle.shape("turtle")

def manecilla():
    for i in range(12):
        turtle.penup()
        turtle.forward(65)
        turtle.pendown()
        turtle.forward(10)
        turtle.penup()
        turtle.forward(25)
        turtle.stamp()
        turtle.backward(100)
        turtle.left(360/12)

manecilla()
