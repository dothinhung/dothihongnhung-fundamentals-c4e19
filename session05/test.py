# dictionary
person = {
    "name": "Quân",
    "age": 22,
    "ex": 2,
    "favs": ["Pes", "Ping pong"]

}

# key = "school"


# # kiểm tra xem key có trong dic k

# if key in person:
#     print(person[key])
# else:
#     print("Not found")


# # thêm 1 cặp key value 

# person['school'] = "Nguyễn Gia Thiều"

# print(person)

### read
# # duyệt dic theo key

# for key in person.keys():
#     print(key, end="\t")


# # duyệt theo cả key cả values

# for key, value in person.items():
#     print(key, value)

# # duyệt theo value

# for value in person.values():
#     print(value)



# #### update

# person['name'] = "Quân kull"
# print(person)

###delete

del person['ex']
print(person)

