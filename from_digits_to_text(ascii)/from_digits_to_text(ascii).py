number = int(input())
char_compilator=""
for _ in range(number):
    number = int(input())
    char_compilator+=chr(number)

print (char_compilator,end='')
