
print("Guess your number game")
print("Now think of a number from 0 to 100, then press 'Enter'")
# an enter de chay tiep // dung console lai
input()

print("""
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's' if my guess is 'S'maller than your number
'l' if my guess is 'L'arger than your number
""")

# print("All you have to do is to answer to my guess")
# print("'c' if my guess is 'C'orrect")
# print("'s' if my guess is 'S'maller than your number")
# print("'l' if my guess is 'L'arger than your number")

low = 0
high = 100
loop = True

while loop:
    mid = (low + high) //2 +1

    guess_numb  = input("Is {0} your number? ".format(mid)).lower()
    

    if guess_numb == 'c':
        print("I knew it")
        break
    elif guess_numb == 's':
        low = mid
        # mid = ((low + high) // 2 + 1 )

    elif guess_numb == 'l':
        high = mid
        # mid = ((low + high) // 2 + 1 )


    







