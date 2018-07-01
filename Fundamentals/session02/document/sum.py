number = int(input("Enter a number: "))
sum = 0
for i in range(number+1):
    sum = sum + i
    print(sum)

# sum() : tinh tổng 1 dãy số
# cách 2
seq = range(number+1)
total = sum(seq)
print(total)

    
