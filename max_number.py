import sys

highest_number = - sys.maxsize

while True:
    numbers = input()
    if numbers == "Stop":
        break
    numbers = int(numbers)

    if numbers >= highest_number:
        highest_number = numbers

print(highest_number)
