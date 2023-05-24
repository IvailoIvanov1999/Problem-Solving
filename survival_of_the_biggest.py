str_integers = input().split()
count_how_many_numbers_to_remove = int(input())

list_new_integers = []

new = []

for el in (str_integers):
    list_new_integers.append(int(el))

for _ in range(count_how_many_numbers_to_remove):
    minimum = min(list_new_integers)
    list_new_integers.remove(minimum)


print(', '.join([str(x) for x in list_new_integers]))

