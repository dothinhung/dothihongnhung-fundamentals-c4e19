# import * là lấy tất cả trong turtle nếu cần dùng đến
from turtle import * 

shape("turtle")
color("red")
speed(-1) 
# speed là cắm tốc độ cho con rùa

for i in range(300):
      for j in range(4):
            forward(100)
            left(90)
     
      right(7)

# # for i in range(100):
# #      forward(100)
# #      left(90)

#  n = int(input("number of side"))
#  for i in range(n):
#      forward(100)
#      left(360/n)

mainloop()