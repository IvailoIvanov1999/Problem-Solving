journal = input().split(", ")



while True:
    comand_input = input().split(" - ")

    comand_move = comand_input[0]

    if comand_move == "Craft!":
        print(", ".join(journal))
        break

    item = comand_input[1]



    if comand_move == "Collect":
        journal.append(item)
        if item in journal:
            set(journal)

            continue



    elif comand_move == "Drop":
        if item in journal:
            journal.remove(item)
        else:
            continue



    if comand_move == "Combine Items":
        list(item)
        itemsss = item.split(":")
        item_1_old = itemsss[0]
        item_2_new = itemsss[1]
        if item_1_old in journal:
            location_old_item = journal.index(item_1_old)
            journal.insert(location_old_item+1,item_2_new)
        else:
            continue



    elif comand_move == "Renew":
        journal.remove(item)
        journal.append(item)




