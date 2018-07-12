strings = input("Enter a sentence: ")

print(strings)

letter_counts = {}
for letter in strings:
    letter_counts[letter] = letter_counts.get(letter, 0) + 1
print(letter_counts, end="\t")
