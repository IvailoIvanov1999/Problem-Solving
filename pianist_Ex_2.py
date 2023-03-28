n = int(input())

collection = {}

for i in range(n):
    text_input = input().split('|')
    p = text_input[0]
    com = text_input[1]
    k = text_input[2]
    collection[p] = [com, k]

command = input()

while not command == "Stop":
    command = command.split('|')
    type_command = command[0]
    piece = command[1]
    if type_command == 'Add':
        composer = command[2]
        key = command[3]
        if piece in collection:
            print(f"{piece} is already in the collection!")
        else:
            collection[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")
    elif type_command == 'Remove':
        if piece in collection:
            del collection[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif type_command == 'ChangeKey':
        new_key = command[2]
        if piece in collection:
            collection[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for piece in collection:
    print(f"{piece} -> Composer: {collection[piece][0]}, Key: {collection[piece][1]}")
