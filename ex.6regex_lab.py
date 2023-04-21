import re

listed = []

while True:
    word = input()

    regex = r"www\.[A-Za-z\-\d]+[\.][a-z\.]+"

    result = re.findall(regex, word)

    listed.extend(result)

    if not word:
        break
for item in listed:
    print(item)
