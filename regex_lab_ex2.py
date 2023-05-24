import re

word = input()

regex = r"\b_[a-zA-Z0-9]+\b"

sorted_word = re.findall(regex,word)
sorted_word = ",".join(sorted_word).replace("_",'')

print(sorted_word)