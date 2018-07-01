print("Hello, my name is Hiep and these are my ship sizes")
original_size = [5, 7, 300, 90, 24, 50, 75]
print(original_size)
print("\t")

biggest = max(original_size)
print("Now my biggest sheep has size {0} let's shear it".format(biggest))
print("\t")

print("After shearing, here is my flock")
new_size = original_size.index(biggest)
original_size[new_size] = 8
print(original_size)
print("\t")

print("One month has passed, now here is my flock")
count = 0
for item in original_size:
    item = item + 50
    original_size[count] = item
    count += 1
print(original_size)
    
    
