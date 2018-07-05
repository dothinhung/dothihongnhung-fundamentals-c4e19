import random 
word = "champion"
original_list = list(word)
print(*original_list, sep="\n")

new_list = []
loop = True
while loop:
    rand_word = random.choice(original_list)
    original_list.remove(rand_word)
    new_list.append(new_list)

    if len(original_list) == 0:
        loop = False

    print(*original_list)

ans = input("Enter your ans: ")

if ans == word:
    print("Hura")
else: 
    print("Try again")


# # ex1 sai
# num = input("Enter a list of number : ")

# n = list(num)
# for index, item in enumerate(n):
#     if index % 2 != 0:
#         n.pop(index) 
#         print(*n, sep="\n")
#         # print(index, item)


# # print(*n, sep="\n")