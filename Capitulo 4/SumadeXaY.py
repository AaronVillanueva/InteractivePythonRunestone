def sumTo(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return (sum)

t = sumTo(0)
print("La suma del 1 al 0 es de",t)
t = sumTo(10)
print("La suma del 1 al 10 es de",t)
t = sumTo(5)
print("La suma del 1 al 5 es de",t)