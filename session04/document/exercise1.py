# bài 1 homework
name = input("Enter your full name: ")

list_name = name.split()
# print(name.capitalize())
# print(*list_name, sep=" ")

print("Update : ", end=" ")

for i in range(len(list_name)):
    print(list_name[i].title(), end=" ")
    

