import turtle 

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")

tess = turtle.Turtle()
tess.color("blue")
tess.pensize(2)

alex = turtle.Turtle()
alex.color("red")

# multi = turtle.Turtle()
# multi.color("blue")

# ew = turtle.Turtle()
# ew.color("red")

# for i in range (3):
#     tess.forward(80)
#     tess.left(120)

# tess.right(180)
# # tess.forward(80)

# for i in range(4):
#     alex.forward(80)
#     alex.left(90)

# for i in range(5):
    
#     multi.forward(80)
#     multi.left(72)

# for i in range(6):
#     ew.forward(80)
#     ew.left(60)

# for i in range(4):
for j in range(2):
        tess.right(30)
        tess.forward(80)
        tess.left(90)

wn.mainloop()