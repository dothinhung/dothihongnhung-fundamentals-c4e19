import turtle

# wn = turtle.Screen()

# triangle = turtle.Turtle()
# triangle.color("blue")

# for i in range(3):
#     triangle.forward(90)
#     triangle.left(120)


# square = turtle.Turtle()
# square.color("red")
# for i in range(4):
#     square.forward(90)
#     square.left(90)

# alex = turtle.Turtle()
# alex.color("blue")
# for i in range(5):
#     alex.forward(90)
#     alex.left(72)

# tess = turtle.Turtle()
# tess.color("red")
# for i in range(6):
#     tess.forward(90)
#     tess.left(60)

# wn.mainloop()

# another way
from turtle import*
color("green")
speed(-1)
edge = 2
for i in range(4):
    edge +=1
    for j in range(edge):
        forward(100)
        left(360/edge)
    if(edge%2==0):
        color("green")
    else:
        color("red")    
   

mainloop()