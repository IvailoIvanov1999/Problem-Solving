import re

word = input()

regexxx = r"(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})"

result = re.findall(regexxx, word)



for el in result:


    print(f"Day: {el[0]}, Month: {el[2]}, Year: {el[3]}")
