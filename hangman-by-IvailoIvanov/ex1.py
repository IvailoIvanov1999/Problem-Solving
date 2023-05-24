import math
from math import ceil
number_of_studens = int(input())
number_of_lectures = int(input())
additional_bonus = int(input())
max_bonus = []
atendances_count_list = []
if number_of_lectures == 0:
    print(f'Max Bonus: 0.')
    print(f'The student has attended 0 lectures.')
    exit()
for _ in range(number_of_studens):
    attendances_count = int(input())
    atendances_count_list.append(attendances_count)

    total_bonus = attendances_count / number_of_lectures * (5 + additional_bonus)
    max_bonus.append(total_bonus)

    maximum_bonus = max(max_bonus)

print(f"Max Bonus: {round(ceil(maximum_bonus))}.")
print(f"The student has attended {(round(ceil(max(atendances_count_list))))} lectures.")