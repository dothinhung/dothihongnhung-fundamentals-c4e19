from turtle import *

col = ["red", "blue", "brown", "yellow", "grey"]

for i in range(5):
    begin_fill()

    for j in range(2):
            forward(50)
            left(90)
            forward(100)
            left(90)
            
    color(col[i])

    forward(50)

    end_fill()



mainloop()