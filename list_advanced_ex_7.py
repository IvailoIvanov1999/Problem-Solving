employees_happiness = [int(x) for x in input().split(" ")]
factor = int(input())
new_list = []

filtred_counter = 0
unhappy = 0

for el in employees_happiness:
    new_list.append(el * factor)

happiness_percent = sum(new_list) // len(employees_happiness)

for num in (new_list):
    number = int(num)

    if number > happiness_percent:
        filtred_counter += 1


if filtred_counter >= len(new_list)/2:
    print(f"Score: {(filtred_counter)}/{len(employees_happiness)}. Employees are happy!")

else:
    print(f"Score: {filtred_counter}/{len(employees_happiness)}. Employees are not happy!")
