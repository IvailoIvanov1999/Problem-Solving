word = input()

char_dict = {}
if " " in word:
    worda = word.split(" ")
    word = "".join(worda)
for char in word:

    if char not in char_dict:
        char_dict[char] = 0
    char_dict[char] += 1
for character in char_dict:
    print(f'{character} -> {char_dict[character]}')
