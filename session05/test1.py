teen_code ={
    "hc": "học",
    "ng": "người",
    "pt": "phát triển",
    "eny": "em người yêu",
    "any": "anh người yêu",
    "ns": "nói",
    "ngta": "người ta",
    "lm": "làm",
    "stt": "status"
}

# if key in teen_code:
#     print(teen_code[key])
# else:
#     print("Not found")

# code = input("Enter your code?: ")

loop = True

while loop:
    for key in teen_code.keys():
        print(key, end="\t")

    code = input("\nEnter your code?: ")

    if code in teen_code:
        print(teen_code[code])
    else:
        check = input("Not found, Do you want to contribute (Y/N)? : ")
        if check == "Y":
            add = input("Your translation?: ")
            teen_code[code] = add
            print("Update: ")
        elif check == "N":
            loop = False
            
