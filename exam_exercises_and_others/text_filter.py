banned_words = input().split(", ")

textt = input()

for w in banned_words:
    while w in textt:
        textt = textt.replace(w, "*" * len(w))

print(textt)
