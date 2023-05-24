number = int(input())

total_sum_1 = 0
total_sum_2 = 0
for i in range(number):
    numbers_1 = int(input())
    total_sum_1 += numbers_1

for i in range(number):
    number_2=int(input())

    total_sum_2 += number_2

if total_sum_1 == total_sum_2:

    print(f"Yes, sum = {total_sum_1}")

else:
    print(f'No, diff = {abs(total_sum_1 - total_sum_2)}')
