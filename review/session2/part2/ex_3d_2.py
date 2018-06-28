n = int(input("Enter a number: "))

for i in range(n):
    for j in range(n):
        if i%2 == 0 and j%2 == 0:
            print("1",end=' ')
        elif i%2 != 0 and j%2 !=0:
            print("1",end=' ')
        else:
            print("0",end=' ')
    print()
    print()