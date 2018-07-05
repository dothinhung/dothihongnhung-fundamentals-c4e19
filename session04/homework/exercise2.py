import locale

balance = int(input("Enter your balance: "))
# print(balance)

locale.setlocale( locale.LC_ALL, '' )

locale.currency(balance)

# locale.currency( balance, grouping = True )

print("Update your balance: ", locale.currency( balance, grouping = True ))

