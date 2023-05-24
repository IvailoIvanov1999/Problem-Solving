num = int(input())

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(num):
    number = int(input())

    if number < 200:
        p1 = p1 + 1


    elif number <= 399:
        p2 = p2 + 1


    elif number <= 599:
        p3 = p3 + 1


    elif number <= 799:
        p4 = p4 + 1


    elif number >= 800:
        p5 = p5 + 1


p1=(p1/num)*100
print(f'{p1:.2f}%')

p2=(p2/num)*100
print(f'{p2:.2f}%')

p3=(p3/num)*100
print(f'{p3:.2f}%')

p4=(p4/num)*100
print(f'{p4:.2f}%')

p5=(p5/num)*100
print(f'{p5:.2f}%')
