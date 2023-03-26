number_of_pieces_to_have = int(input())

dict_the_pianist = {}

for _ in range(number_of_pieces_to_have):
    pieces = input().split("|")
    piece = pieces[0]
    composer = pieces[1]
    key = pieces[2]
    dict_the_pianist[piece] = [composer, key]

command_entry = input()
while command_entry != "Stop":

    comands_splited = command_entry.split("|")
    type_comm = comands_splited[0]
    piece_universal = comands_splited[1]
    # Add
    if type_comm == "Add":
        composer_add = comands_splited[2]
        key_add = comands_splited[3]
        if piece_universal in dict_the_pianist:
            print(f"{piece_universal} is already in the collection!")
        else:
            dict_the_pianist[piece_universal] = [composer_add, key_add]
            print(f"{piece_universal} by {composer_add} in {key_add} added to the collection!")
   # Remove
    elif type_comm == "Remove":
        if piece_universal in dict_the_pianist:
            del dict_the_pianist[piece_universal]
            print(f"Successfully removed {piece_universal}!")
        else:
            print(f"Invalid operation! {piece_universal} does not exist in the collection.")
    # Change
    elif type_comm == "ChangeKey":
        new_key_change = comands_splited[2]
        if piece_universal in dict_the_pianist:
            dict_the_pianist[piece_universal][1] = new_key_change

            print(f"Changed the key of {piece_universal} to {new_key_change}!")

        else:
            print(f"Invalid operation! {piece_universal} does not exist in the collection.")
    command_entry = input()

for keysssss in dict_the_pianist:
    print(f"{keysssss} -> Composer: {dict_the_pianist[keysssss][0]}, Key: {dict_the_pianist[keysssss][1]}")
