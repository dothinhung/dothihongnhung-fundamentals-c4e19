loop = True
item = ["T-Shirt", "Sweater"]

while loop:
    choice = input("Welcome to our shop, what do you want (C, R, U, D)? : ")

    if choice == "R":
        print("Our items : ", end =" ")
        print(*item, sep =", ")

    elif choice == "C":
        add_new_item = input("Enter new item: ")
        item.append(add_new_item)
        print("Our items : ", end =" ")
        print(*item, sep =", ")

    elif choice == "U":
        while True:
            pos = int(input("Update position? : "))
            if pos > len(item):
                print("Invalid position!!!")
            else:
                update_item = input("New item?: ")
                item[pos - 1] = update_item
                print("Our items : ", end =" ")
                print(*item, sep =", ")
                break
                

    elif choice == "D":
        while True:
            del_item = int(input("Delete position? : "))
            if del_item > len(item):
                print("Invalid position!!!")
            else:
                item.pop(del_item -1)
                print("Our items : ", end =" ")
                print(*item, sep =", ")
                break
                
    elif choice == "No" or choice == "no":
        loop = False

    else:
        print("You must following suggestion")
        
        

        

 
    

