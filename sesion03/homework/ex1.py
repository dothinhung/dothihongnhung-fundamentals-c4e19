loop = True
choice = ["C", "R", "U", "D"]
item = ["T-Shirt", "Sweater"]
while loop:

    for (i) in choice:
        n = input("Welcome to our shop, what do you want (C, R, U, D)? : ")
        if n == choice[1]:
            print("Our items : ", end =" ")
            print(*item, sep =", ")
            

        elif n == choice[0]:
            add_new_item = input("Enter new item: ")
            item.append(add_new_item)
            print("Our items : ", end =" ")
            print(*item, sep =", ")
            

        elif n == choice[2]:
            pos = int(input("Update position? : "))
            update_item = input("New item?: ")
            item[pos - 1] = update_item
            print("Our items : ", end =" ")
            print(*item, sep =", ")

        elif n == choice[3]:
            del_item = int(input("Delete position? : "))
            item.pop(del_item -1)
            print("Our items : ", end =" ")
            print(*item, sep =", ")
            
        else:
            print("You must following suggestion")
    loop = False       
    
    