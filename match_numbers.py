import re
word = input()
regex = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))"

result=re.finditer(regex,word)
for item in result:

    print(item.group(),end=" ")