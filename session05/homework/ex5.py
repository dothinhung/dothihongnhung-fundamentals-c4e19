prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

total = 0

for key in prices.keys():
    print("\n",key)
    print("price: ", prices[key])
    print("stock: ", stock[key])
    mul = prices[key]*stock[key]
    print("Multiply = ",mul)
    total += mul

print("\n")
print("Total = ", total)


