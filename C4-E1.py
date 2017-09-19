import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")

andii = turtle.Turtle()
andii.color("purple")

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