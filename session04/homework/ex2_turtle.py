from turtle import *

color("blue")
speed(-1)
size = 5

n = int(input("Enter a number: "))

for i in range(n):
    for j in range(4):
        forward(size)
        left(90)

    left(360/n)
    size = size + 2

mainloop()