import turtle
# create playground for turtle
wn = turtle.Screen() 
# set up color for windown
wn.bgcolor("lightgreen")
# set the windown title
wn.title("Hello, Tess!")

# create turtle and assign to tess 
tess = turtle.Turtle()
# change color
tess.color("blue")
# change size 
tess.pensize(3)

tess.forward(50)
tess.left(120)
tess.forward(50)

wn.mainloop()
