phonebook = {}
n = 0
while True:
    entry = input()
    parts = entry.split("-")
    if len(parts) == 1:
        n = int(entry)
        break

    key = parts[0]
    value = parts[1]
    phonebook[key] = value

for _ in range(n):
    new_names = input()

    if new_names not in phonebook:
        print(f"Contact {new_names} does not exist.")
    else:
        print(f"{new_names} -> {phonebook[new_names]}")
