rows, columns = [int(x) for x in input().split()]
f_lett = 97
matrix = []

for r in range(rows):
    subb = []
    for c in range(columns):
        middle = r + c
        result = chr(f_lett + r) + chr(f_lett +r +c) + chr(f_lett+r)
        subb.append(result)
    print(*subb)






