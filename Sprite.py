import turtle

wn = turtle.Screen()

Maki = turtle.Turtle()
Maki.shape("triangle")

n = int(input("How many legs should this sprite have? "))
angle = 360 / n

for i in range(n):
    Maki.right(angle)
    Maki.forward(65)
    Maki.stamp()
    
    Maki.right(180)
    Maki.forward(65)
    Maki.right(180)

Maki.shape("circle")

wn.exitonclick()
