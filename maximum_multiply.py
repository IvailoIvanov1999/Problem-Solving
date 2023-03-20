divisor=float(input())

boundary=int(input())

last_num=0

for number in range(boundary+1):
    if number%divisor==0:
        last_num=number
print(last_num)