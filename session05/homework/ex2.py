numbers = [1, 6, 8, 1, 2, 1, 5, 6]
print("numbers = ", numbers)

print()
print("The first way")

loop = True
while loop:
    digit = int(input("Enter a number? "))
    count = 0
    for item in numbers:
        if item == digit:
            count += 1
    print(digit, "appears {0} time(s) in my list ".format(count))

    ex = input("Do you want to continue (Y/N)? ").upper()
    print()
    if ex == "Y" and "y":
        loop = True
    elif ex == "N" and "n":
        loop = False


print("========================")
print("The second way")
while True:
    numb = int(input("Enter a number: "))
    for val in numbers:
        if val == numb:
            count = numbers.count(val)
    print("{0} appears {1} time(s) in my list".format(numb, count))


    

