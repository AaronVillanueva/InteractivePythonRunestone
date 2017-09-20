import math

def areaCirculo(radio):
    area= math.pi * (radio**2)
    return(area)

def Main():
    area=areaCirculo(5)
    print(area)

Main()