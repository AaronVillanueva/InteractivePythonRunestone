import turtle

def dibujarEstrella(t):
    for i in range(5):
        t.forward(100)
        t.left(216)

def separacion(t):
    t.penup()
    t.forward(350)
    t.right(144)
    t.pendown()

Maki = turtle.Turtle()
for i in range(5):
    dibujarEstrella(Maki)
    separacion(Maki)
