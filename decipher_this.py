message = input().split(' ')
result = []

for word in message:
    ascii_char = [char for char in word if char.isdigit()]
    word_str = [char for char in word if char.isalpha()]

    first_letter = chr(int(''.join(ascii_char)))
    word_str[0], word_str[-1] = word_str[-1], word_str[0]
    new_word = first_letter + ''.join(word_str)
    result.append(new_word)

print(' '.join(result))