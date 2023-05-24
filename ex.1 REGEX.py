import re
word = input()

regex_word = r'\b[A-Z][a-z]+ [A-Z][a-z]+\b'

result = re.findall(regex_word,word)

print(" ".join(result))