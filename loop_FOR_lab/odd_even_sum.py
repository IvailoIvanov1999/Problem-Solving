numbers=int(input())

even_num=0
odd_num=0

for i in range(1,numbers+1):
    numbers_count=int(input())
    if i %2==0:
        even_num+=numbers_count
    else:
        odd_num+=numbers_count

if even_num==odd_num:
    print("Yes")
    print(f'Sum = {even_num}')
else:
    print("No")
    print(f'Diff = {abs(even_num-odd_num)}')