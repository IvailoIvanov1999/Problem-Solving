word = input()
splited = word.split(">")
prev = 0
result = [splited[0]]
for part in splited[1:]:
    power = int(part[0])

    prev += power

    formated_part = part[prev:]

    prev = max(prev - len(part),0)
    result.append(formated_part)
print(">".join(result))
