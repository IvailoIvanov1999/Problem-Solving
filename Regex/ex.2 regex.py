import re

word = input()

regexx = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'

results = re.findall(regexx,word)

print(", ".join(results))