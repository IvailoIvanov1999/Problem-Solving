n_times = int(input())

even_list = []
odd_list = []
positive_list = []
negative_list = []

for _ in range(n_times):
    number = int(input())

    if number < 0:
        negative_list.append(number)
    if number == 0:
        even_list.append(number)
    if number >= 0:
        positive_list.append(number)
    if number % 2 == 0:
        even_list.append(number)
    else:
        odd_list.append(number)

comand = input()

if comand == "even":
    print(even_list)
elif comand == "odd":
    print(odd_list)
elif comand == "positive":
    print(positive_list)
else:
    print(negative_list)
