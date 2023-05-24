c_words = int(input())
dictionary = {}

for w in range(c_words):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = []

    dictionary[word].append(synonym)

for wordss in dictionary:
    print(f'{wordss} - {", ".join(dictionary[wordss])}')
