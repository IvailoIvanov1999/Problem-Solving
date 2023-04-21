word = input()

emoticon = []
indexx = 0
for el in word:
    indexx += 1
    if el == ":":
        emoticon.append(word[indexx])
for elements in emoticon:
    print(f":{' '.join(elements)}")
