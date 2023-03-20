import re

final = []
while True:
    word = input()
    if not word:
        break
    regex = r'\d+'
    compiled = re.compile(regex)
    new_word = compiled.findall(word)
    final.extend(new_word)

print(*final, sep=" ")
