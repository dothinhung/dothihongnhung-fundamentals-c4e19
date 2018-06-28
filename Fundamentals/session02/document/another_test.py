yob = int(input("Your date of birth: "))

age = 2018 - yob

if age < 10:
    print("Baby")
elif age < 18:
    print("Teenager")
else:
    print("Not Baby")