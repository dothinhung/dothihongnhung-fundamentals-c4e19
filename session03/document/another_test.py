# food1 = "Kem"
# food2 = "Xoi"
# food3 = "Pho" 
# food4 = "Tao Pho"

# List / array
menu = ["Kem", "Xoi", "Pho", "Thit", "Tao pho"]

# seperator
# print(*menu, sep=",")
# print(len(menu))

# lay ten cua phan tu
# item = menu[-1]
# print(item)

# # them thong tin vao list
# menu.append("Che")
# print(*menu, sep=", ")
# # kiem tra do dai cua list
# print(len(menu))

# duyet ca list dung for nhung it dung trong python
# for i in range(len(menu)):
#     print(menu[i])

# vong for duyet theo tt
# for index, item in enumerate(menu):
#     print(index, item)


# 
# for item in menu:
#     print(item)

menu[1] = "Che"
print(*menu, sep=", ")

# 1 way xoa theo item
# thêm dấu * trước menu là để bỏ []
menu.remove("Kem")
print(*menu, sep=", ")

# 2 way xoas theo index
del menu[1]
print(*menu, sep=", ")

# 3 way
menu.pop(1)
print(*menu, sep=", ")

