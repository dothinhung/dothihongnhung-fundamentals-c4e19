from turtle import *

n = int(input("Enter a number: "))

color("blue")
speed(-1)

for j in range(n):

    for i in range(4):
        forward(100)
        left(90)
        
    right(360/n)
    
    
    
    
mainloop()

