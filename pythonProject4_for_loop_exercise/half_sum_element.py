import sys

num = int(input())

total_number_result = 0
all_num_sum=0
maximum_value = -sys.maxsize

for i in range(1, num + 1):
    numbers_count = int(input())

    total_number_result = total_number_result + numbers_count

    if numbers_count > maximum_value:
        maximum_value = numbers_count


all_num_sum=total_number_result - maximum_value



if maximum_value==all_num_sum:
    print("Yes")
    print(f"Sum = {all_num_sum}")

else:
    print("No")
    diff=all_num_sum-maximum_value
    print(f'Diff = {abs(diff)}')



