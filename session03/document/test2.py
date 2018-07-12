from random import randint
number = randint(0, 100)
print(number)
loop = True
count = 0
while loop:
    gess = int(input("Gess my number: "))
    if gess == number :
        print ("bingo")
    elif gess > number:
        print("Too large")
    else:
        print("Too small")
    
    count += 1
    if count == 7:
        print("You lose")

    loop = False
    

    #  trò chơi đoán số

    
