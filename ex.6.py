word = input()
new_word = word[0]

for char in word:
    if char == new_word[-1]:
        continue

    new_word += char
print(new_word)
