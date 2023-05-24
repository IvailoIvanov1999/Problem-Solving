number_input = [float(x) for x in input().split()]
numbers = 0
rounded_numbers = []


def rounded():
    for num in number_input:
        numbers = round(num)
        rounded_numbers.append(numbers)
    print(rounded_numbers)

rounded()


