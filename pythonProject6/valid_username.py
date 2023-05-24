from string import ascii_letters,digits

username = input().split(", ")

valid = []

alowed_char = ascii_letters + digits + "-" + "_"

for word in username:

    if 3 > len(word) or len(word) > 16:

        continue

    valid_f_t = [ch in alowed_char for ch in word]
    cont_allowed = all(valid_f_t)

    if not cont_allowed:
        continue


    print(word)
