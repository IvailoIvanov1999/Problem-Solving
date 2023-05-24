nums_as_string = input().split()
converted_numbers = []
for num in nums_as_string:
    number = int(num)
    converted_numbers.append(-number)

print(converted_numbers)
