coffees_list_in_stock = input().split()
number_of_commands = int(input())



for _ in range(number_of_commands):
    commands_input = input().split()
    comand = commands_input[0]

    if comand == "Include":
        coffees_list_in_stock.append(commands_input[1])

    elif comand == "Remove":
        if len(coffees_list_in_stock) < int(commands_input[2]):
            continue

        elif commands_input[1] == "first":
            for _ in range(int(commands_input[2])):
                coffees_list_in_stock.remove(coffees_list_in_stock[0])

        elif commands_input[1] == "last":
            for _ in range(int(commands_input[2])):
                coffees_list_in_stock.remove(coffees_list_in_stock[-1])

    elif comand == "Prefer":
        if (int(commands_input[1]) >= 0 and int(commands_input[1]) < len(coffees_list_in_stock)) or (int(
                commands_input[2]) >= 0 and int(commands_input[2]) < len(coffees_list_in_stock)):

            coffees_list_in_stock[int(commands_input[1])], coffees_list_in_stock[int(commands_input[2])] = coffees_list_in_stock[int(commands_input[2])], \
                                                                                                           coffees_list_in_stock[int(commands_input[1])]
        else:
            continue

    elif comand == "Reverse":
        coffees_list_in_stock.reverse()

print("Coffees:")
print(f"{' '.join(coffees_list_in_stock)}")