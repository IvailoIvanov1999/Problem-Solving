number = int(input())

calculated_numbers = 0

while True:
    new_number = int(input())
    calculated_numbers = calculated_numbers + new_number
    if calculated_numbers >= number:

        print(f"{calculated_numbers}")

        break