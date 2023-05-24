
def char(start,end):

    word_1 = ''
    for w in range(ord(first)+1, ord(second)):
        word_1 += f'{chr(w)} '

    print(f'{word_1}')

first = input()
second = input()

char(first,second)