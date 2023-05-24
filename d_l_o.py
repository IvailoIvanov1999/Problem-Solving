word = input()

numbers=[]
letters = []
symbols = []

for l in word:
    if l.isdigit():
        numbers.append(l)
    elif l.isalpha():
        letters.append(l)
    else:
        symbols.append(l)

print("".join(numbers))
print("".join(letters))
print("".join(symbols))

