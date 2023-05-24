str_numbers = input().split(", ")

numbers_as_int = []
no_zero = []
zero_list_2 = []

for n in (str_numbers):
    n_idx = int(n)

    numbers_as_int.append(n_idx)

for number in range(len(str_numbers)):
    if numbers_as_int[number] != 0:
        no_zero.append(numbers_as_int[number])
    else:
        zero_list_2.append(numbers_as_int[number])

print(no_zero + zero_list_2)
