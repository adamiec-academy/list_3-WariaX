from turtle import *

speed ("fast")

a = 200
b = 100

def prostokat(a, b):
    for _ in range(1):
        forward(a)
        left(120)
        forward(a)
        left(120)
        forward(a)
        forward(b)
        right(120)
        forward(b)
        right(120)
        forward(b)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)
        left(90)
        forward(50)



ilosc = 50
kat = 360/ilosc

for _ in range(ilosc):
    prostokat(a, b)
    left(kat)




exitonclick()
