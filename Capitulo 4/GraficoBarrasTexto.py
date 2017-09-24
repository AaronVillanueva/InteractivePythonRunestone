import turtle

xs = [48, 117, 200, 240, 160, 260, 220]
maxheight = max(xs)
numbars = len(xs)
border = 10

wn = turtle.Screen()
wn.setworldcoordinates(0-border, 0-border, 40*numbars+border, maxheight+border)
wn.bgcolor("white")

Maki = turtle.Turtle()
Maki.color("blue")
Maki.fillcolor("red")
Maki.pensize(3)

def drawBar(t, height):
    t.begin_fill()
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()
    t.penup()
    t.speed(0)
    t.backward(40)
    t.left(90)
    t.forward(height+10)
    t.right(90)
    t.forward(10)
    t.write(str(height))
    t.backward(10)
    t.left(90)
    t.backward(10)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.pendown()
    t.speed(3)

for a in xs:
    drawBar(Maki, a)

wn.exitonclick()