sub_word = input().split(", ")
words = input().split(", ")
subwords = []
for sub in sub_word:
    for w in words:
        if sub in w:
            subwords.append(sub)
            break
print(subwords)
