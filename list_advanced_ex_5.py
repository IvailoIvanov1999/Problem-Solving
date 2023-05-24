names = input().split(", ")

names_new = sorted(names, key=lambda x: (-len(x), x))

print(names_new)
