size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Hiep and here is my flock", size)

month = int(input("Number of month(s): "))

for i in range(month):
    print("Month ", i + 1, ": ")
    print("One month passed, now here is my flock")

    count = 0
    for item in size:
        item = item + 50
        size[count] = item
        count += 1
    print(size)

    # biggest size
    biggest = max(size)
    print("Now my biggest sheep has size {0} let's shear it".format(biggest))

    # update size
    new_size = size.index(biggest)
    size[new_size] = 8
    print("After shearing, here is my flock", size)


    





    

