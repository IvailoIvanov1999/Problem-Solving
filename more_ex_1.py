def data_type(command, word):
    if command == 'int':
        word_int = int(word)
        word_int_1 = word_int * 2
        return word_int_1
    elif command == 'real':
        word_real = float(word)
        word_real_1 = (f'{word_real * 1.5:.2f}')
        return word_real_1
    elif command == 'string':
        word_string = word
        word_string_1 = (f'${word_string}$')
        return word_string_1

given_word = input()
number_given = input()


print(data_type(given_word,number_given))



