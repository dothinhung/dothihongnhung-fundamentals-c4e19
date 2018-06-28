# hinh thuan
# for i in range(1, 5):
#     for j in range(i):
#         print("* ", end='')
#     print()

# hinh nguoc

n = 10
for i in range(n):
    # draw 1 line 
    for j in range(n):
        if (j < n - i - 1):
            print(" ", end='')
        else:
            print("* ", end='')
    print()
