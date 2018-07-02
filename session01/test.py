# Bài 1: Nhập vào 1 dãy số và in dãy số vừa nhập mỗi số 1 hàng
# Bài 2: cho 1 dãy số, tính xem tích của cặp số nào bằng 128, nếu bằng 128 in ra số thứ tự của số dó


# Ex2:
list = ["1", "2", "24", "34", "5", "64", "128"]
print("Day so cho san:", end=" ")
print(*list, sep=", ")

# for index1, item1 in enumerate(list):
#     for index2, item2 in enumerate(list):
#         item = int(item1) * int(item2)
#         print(item)

# for item1 in list:
#     for item2 in list:
#         # print(item2)
#         item = int(item1) * int(item2)
#         if item == 128:
#             print(item)
#     # print(item1)

for index1, item1 in enumerate(list):
    for index2, item2 in enumerate(list):
        item = int(item1) * int(item2)
        if item == 128:
            # print(item1, index1)
            print("ở vị trí thứ {0} và {1}".format(index1 +1 , index2 + 1))