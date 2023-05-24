numbers = [int(el) for el in input().split(", ")]
print([elem for elem in range(len(numbers)) if numbers[elem] % 2 == 0])



