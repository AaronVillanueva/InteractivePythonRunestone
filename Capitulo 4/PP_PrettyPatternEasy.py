import turtle

wn = turtle.Screen()
wn.bgcolor("white")
Maki = turtle.Turtle()
Maki.color('red')
Maki.pensize(3)
Maki.speed(10)

def cuadrado(t,lado):
    for i in range(4):
        for i in range(4):
            t.forward(lado)
            t.right(90)
        t.right(90)
def Main():
    for i in range(6):
        cuadrado(Maki,50)
        Maki.right(360/24)

Main()