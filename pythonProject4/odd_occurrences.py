words = input().split(" ")
dictionary = {}
counter_times = 0
for w in words:
    words_lowered = w.lower()

    if words_lowered not in dictionary:
        dictionary[words_lowered] = 0
    dictionary[words_lowered] += 1

for key, value in dictionary.items():
    if value % 2 != 0:
        print(key, end=" ")
