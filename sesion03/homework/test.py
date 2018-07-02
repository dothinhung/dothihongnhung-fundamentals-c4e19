# Đề bài : cho 1 dãy số 1, 2, 24, 34, 5, 64, 128
# tìm cặp số có tích bằng 128, 
# nếu tích bằng 128 thì in ra số và vị trí của số đó trong dãy số
list = ["1", "2", "24", "34", "5", "64", "128"]
print("Cho dãy số sau: ", end=" ")
print(*list, sep=", ")


for index1, item1 in enumerate(list):
    for index2, item2 in enumerate(list):
        item = int(item1) * int(item2)
        if item == 128:
            print("Cặp số có tích bằng 128 là số {0} * {1} ở vị trí thứ {2} và {3}".format(item1, item2, index1 +1 , index2 + 1))