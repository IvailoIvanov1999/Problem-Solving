from os.path import exists
from os import remove

while True:
    command = input()
    if command == "End":
        break

    split_command = command.split("-")
    action = split_command[0]
    file_name = split_command[1]



    if action == "Create":
        file = open(f'{file_name}', 'w')
        file.close()

    elif action == "Add":
        content = split_command[2]
        file = open(f'{file_name}', 'a')
        file.write(f"{content}\n")
        file.close()

    elif action == "Replace":
        try:
            file = open(f'{file_name}', 'r')
            text = file.readlines()
            old_string = split_command[2]
            new_string = split_command[3]
            for i in range(len(text)):
                text[i] = text[i].replace(old_string, new_string)
            with open(f'{file_name}', 'w') as file:
                file.write(''.join(text))
        except FileNotFoundError:
            print("An error occurred")

    elif action == "Delete":
        try:
            remove(file_name)

        except FileNotFoundError:
            print("An error occurred")