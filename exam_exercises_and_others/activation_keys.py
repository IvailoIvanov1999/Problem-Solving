activation_key = input()

while True:
    command = input().split(">>>")
    action = command[0]

    if action == "Generate":
        break

    if action == "Contains":
        substring = command[1]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif action == "Flip":
        start_index = int(command[2])
        end_index = int(command[3])

        word_to_be_changed = activation_key[start_index:end_index]

        if command[1] == "Upper":
            activation_key = activation_key[:start_index] + f"{word_to_be_changed.upper()}" + activation_key[end_index:]
        elif command[1] == "Lower":
            activation_key = activation_key[:start_index] + f"{word_to_be_changed.lower()}" + activation_key[end_index:]
        print(activation_key)

    elif action == "Slice":
        start_i_slice = int(command[1])
        end_i_slice = int(command[2])
        subs_to_delete = activation_key[start_i_slice:end_i_slice]

        activation_key = activation_key.replace(subs_to_delete, "")
        print(activation_key)


print(f"Your activation key is: {activation_key}")