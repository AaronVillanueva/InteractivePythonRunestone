import turtle

wn = turtle.Screen()
wn.bgcolor("white")
Maki = turtle.Turtle()
Maki.color('red')
Maki.pensize(3)

def relojInicial(t, manecilla):
    for i in range(24):
        t.forward(manecilla)
        t.backward(manecilla)
        t.right(360/24)
def circulo(t):
    t.circle(50)

def cuadrado(t,lado):
    for i in range(4):
        t.forward(lado)
        t.right(90)

def reposicionar(t):
    t.penup()
    t.home()
    t.pendown()

def Main():
    relojInicial(Maki,50)
    Maki.left(90)
    Maki.backward(50)
    Maki.right(90)
    circulo(Maki)
    reposicionar(Maki)
    Maki.forward(50)
    Maki.right(90)
    cuadrado(Maki,100)
Main()