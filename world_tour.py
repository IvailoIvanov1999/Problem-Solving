word_all_destinations = input()

while True:
    command = input()
    if command == "Travel":
        break
    split_command = command.split(":")

    action = split_command[0]

    if action == "Add Stop":
        index = int(split_command[1])
        string_to_add = split_command[2]
        if len(word_all_destinations) >= index:
            word_all_destinations = word_all_destinations[:index] + f"{string_to_add}" + word_all_destinations[index:]



    elif action == "Remove Stop":
        start_index = int(split_command[1])
        end_index = int(split_command[2])
        if start_index in range(len(word_all_destinations)) and end_index in range(len(word_all_destinations)):
            # if start_index >
            to_remove = word_all_destinations[start_index:end_index + 1]

            word_all_destinations = word_all_destinations[:start_index] + word_all_destinations[end_index + 1:]



    elif action == "Switch":
        old_string = split_command[1]
        new_string = split_command[2]

        if old_string in word_all_destinations:
            word_all_destinations = word_all_destinations.replace(old_string, new_string)

    print(word_all_destinations)

print(f"Ready for world tour! Planned stops: {word_all_destinations}")
