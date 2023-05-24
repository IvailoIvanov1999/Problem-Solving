while True:
    insert = input()

    if insert == "End":
        break
    if insert == "SoftUni":
        continue


    for ch in (insert):
        print(ch, end="")
        for w in (ch):
            print(w, end="")

    print()
