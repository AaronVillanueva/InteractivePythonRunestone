import turtle

wn = turtle.Screen()
wn.bgcolor("white")

andii = turtle.Turtle()
andii.color("red")

def dibujarCuadrado(t, lado):
    for i in range(4):
        t.forward(lado)
        t.left(90)
    t.forward(lado)
    t.penup()
    t.forward(lado)
    t.pendown()

for i in range(5):
    dibujarCuadrado(andii, 20)

wn.exitonclick()