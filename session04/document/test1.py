# test prime number
# co the dung for

numb = int(input("Enter a number: "))

is_prime = True

# for i in range(2, numb - 1):
#     if numb % i == 0:
#         print("not prime number")
#     else:
#         print("prime number")
i = 2

if numb < 2:
    print("{0} is not a prime number".format(numb))

else:
    while i <= (numb ** 0.5):
        if numb % i == 0:
            is_prime = False
            break
        i += 1  
    if is_prime:
        print("{0} is a prime number".format(numb))
    else:
        print("{0} is not a prime number".format(numb))
 



