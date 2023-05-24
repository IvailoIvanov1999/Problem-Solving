num_of_times = int(input())

positive_numbers_list = []
negative_numbers_list = []
counter_positives = 0
for el in range(num_of_times):
    numbers = int(input())
    if numbers <= 0:
        negative_numbers_list.append(numbers)

    else:
        positive_numbers_list.append(numbers)
        counter_positives += 1

print(positive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {counter_positives}")
print(f"Sum of negatives: {sum(negative_numbers_list)}")
