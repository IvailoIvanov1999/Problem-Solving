groceries_ls = input().split("!")

while True:
    command_input = input().split()


    command = command_input[0]
    item = command_input[1]
    comand_str=' '.join(command_input)
    if comand_str == "Go Shopping!":
         break

    elif command == "Urgent":
        if item in groceries_ls:
            continue
        else:
            groceries_ls.insert(0, item)

    elif command == "Unnecessary":
        if item in groceries_ls:
            groceries_ls.remove(item)
        else:
            continue

    if command == "Correct":
        list(command_input)

        item_1_old = command_input[1]
        item_2_new_one = command_input[2]

        if item_1_old in groceries_ls:
            location_old = groceries_ls.index(item_1_old)
            groceries_ls.remove(item_1_old)
            groceries_ls.insert(location_old,item_2_new_one)
        else:
            continue

    elif command == "Rearrange":
        if item in groceries_ls:
            # location = groceries_ls.index_life(item)
            groceries_ls.remove(item)
            groceries_ls.append(item)
        else:
            continue

print(", ".join(groceries_ls))