from turtle import *
speed(-1)
col = ["red", "blue", "brown", "yellow", "grey"]
size = 3

for i in range(5):

    for j in range(size):
        forward(100)
        left(360/size)

        color(col[i])
        
    size += 1



mainloop()