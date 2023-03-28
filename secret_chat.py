message = input()
counter_appearances = 0
while True:
    command = input().split(":|:")
    action = command[0]

    if action == "Reveal":
        break

    if action == "InsertSpace":
        index_for_space = int(command[1])
        message = message[:index_for_space] + " " + message[index_for_space:]
        print(message)

    elif action == "Reverse":
        subs = command[1]

        if subs in message:
            reversed_sub = subs[::-1]
            message = message.replace(subs,reversed_sub,1)
            message = message.replace(reversed_sub,"",1)
            message = message + reversed_sub
            # subs_for_cut = message[len(subs):]
            #
            #
            # subs_for_cut_2 = subs_for_cut[len(subs) - 2:]
            #
            # subs_for_cut_3 = subs_for_cut_2[::-1]
            #
            # message = to_cut
            print(message)
        else:
            print("error")

    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        message = message.replace(substring, replacement)

        print(message)

print(f"You have a new text message: {message}")
