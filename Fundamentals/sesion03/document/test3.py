number = int(input("Enter a number: "))
original_numb = number
print(number)
loop = True
count = 0

#  có thể tạo đk number > 0 thay cho loop
while loop:
    number = number // 10
    if number == 0:
        loop = False

    count += 1

print("{0} has {1} digit(s)".format(original_numb, count))
        