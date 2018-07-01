n = 9

for i in range(n):
    for j in range(n):
        if i%2 == 0 and j%2 == 0:
            print("1", end=' ')
        elif i%2 != 0 and j%2 != 0:
            print("1", end=' ')
        else:
            print("0",end=' ')
    print()
    print()


#######
n = 9
for i in range(n):
    if (i%2==0):
        for j in range(n):
            if(j%2==0):
                print(" 1 ", end = "")
            else:
                print(" 0 ", end = "")
        print("")
    else:
        for j in range(n):
            if(j%2 == 0):
                print(" 0 ", end = "")
            else:
                print(" 1 ", end = "")
        print("")

    
  
