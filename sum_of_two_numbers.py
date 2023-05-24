start = int(input())
finish = int(input())
magic_number = int(input())
counter = 0
flag=False

for n in range(start, finish+1):
    for b in range(start,finish+1):
        counter += 1

        total = n + b

        if total == magic_number:
            print(f"Combination N:{counter} ({n} + {b} = {magic_number})")
            flag=True
    if flag:
        break

if not flag:
    print(f"{counter} combinations - neither equals {magic_number}")