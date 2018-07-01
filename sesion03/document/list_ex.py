print("Hi there, ........")
menu = ["death note", "netflix", "teaching"]
# print(*menu, sep=", ")

# python theo snake case
# name = input("Name one thing you want to add?: ")
# menu.append(name)
# print(*menu, sep=", ")

for index, item in enumerate(menu):
    print(index + 1, item, sep=". ")

pos = int(input("Position you want to update: "))
update_menu = input("Your replacing menu: ")

menu[pos - 1] = update_menu


print(*menu,sep=", ")
    