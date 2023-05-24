year_tax = int(input())

shoes = year_tax - (year_tax * 0.40)

clothes = shoes - (shoes * 0.20)

ball = clothes / 4

accessories = ball / 5

all_sum = shoes + clothes + ball + accessories + year_tax

print(all_sum)
