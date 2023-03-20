import re

word = input().lower()

searched_word = input().lower()

regex = rf"\b{searched_word}\b"

done = re.findall(regex,word)

print(len(done))

