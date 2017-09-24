def determinarBisiesto(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                conclusion=True
            else:
                conclusion=False
        else:
            conclusion=True
    else:
        conclusion=False
    return(conclusion)

def Main():
    year=int(input("Ingrese un año para determinar si es bisiesto: "))
    print(determinarBisiesto(year))

Main()