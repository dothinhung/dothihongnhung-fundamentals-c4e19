inventory = {
    "gold": 500,
    "pouch": ['flint', 'twine', 'gemstone'],
    "backpack" : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}

print("Inventory after add  ")
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
print(inventory)
print()

print("Inventory after remove dagger ")
inventory['backpack'].remove('dagger')
print(inventory)
print()

print("Inventory after add 50 ")
inventory['gold'] += 50
print(inventory)



