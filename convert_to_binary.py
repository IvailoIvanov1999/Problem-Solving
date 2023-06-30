content = int(input("Input a character to convert: "))
try:
    num = int(content)
except ValueError:
    num = ord(str(content))

final = []
while num != 0:
    n = num % 2
    n %= 2
    if n != 0:

        final.append("1")
    else:

        final.append("0")
    num = num // 2

print(final[::-1])
