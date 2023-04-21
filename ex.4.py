word_in = input()
new_el = 0
new_word = ""
for el in word_in:
    q = ord(el)
    new_el = ord(el)+3
    char_i = chr(new_el)
    new_word += char_i

print(new_word)