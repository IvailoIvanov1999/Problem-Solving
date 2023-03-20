number_strings=int(input())

for _ in range (number_strings):
    string_input=input()
    flag=True
    for ch in (string_input):
        if ch=="." or ch=="," or ch=="_":
            flag=False
            break


    if flag:
        print(f"{string_input} is pure.")
    else:
        print(f"{string_input} is not pure!")