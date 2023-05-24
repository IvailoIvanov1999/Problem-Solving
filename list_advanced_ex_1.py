word = [el for el in input() if el.lower() not in ['a', 'o', 'u', 'e', 'i']]
print("".join(word))
