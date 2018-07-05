from turtle import *

color("blue")



for i in range(10):
    for j in range(4):
        forward(50)
        left(90)
        
    right(10)
    forward(5*i)

mainloop()