import turtle

wn = turtle.Screen()
wn.bgcolor("white")
Maki = turtle.Turtle()

def dibujarAdorno(t, numeroPiernas, longitudPiernas):
   angulo = 360/numeroPiernas
   for i in range(numeroPiernas):
      t.forward(longitudPiernas)
      t.backward(longitudPiernas)
      t.left(angulo)

def dibujarCuadrado(t, sz, piernas, longitud):
   for i in range(4):
       t.forward(sz)
       dibujarAdorno(t, piernas, longitud)
       t.left(90)

def Main():
    dibujarCuadrado(Maki, 100, 10, 15)

Main()
wn.exitonclick()