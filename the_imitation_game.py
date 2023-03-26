word_encrypted_message = input()
items_char_to_move = ''
while True:

    instructions = input().split("|")

    if instructions[0] == "Decode":
        break

    command = instructions[0]

    if command == "Move":
        times_move = int(instructions[1])
        subss_to_move = word_encrypted_message[:times_move]
        word_encrypted_message = word_encrypted_message[times_move:] + f"{subss_to_move}"


    elif command == "Insert":
        indexx = int(instructions[1])
        value = instructions[2]

        word_encrypted_message = word_encrypted_message[:indexx] + f"{value}" + word_encrypted_message[indexx:]

    elif command == "ChangeAll":
        subs = instructions[1]
        repl = instructions[2]

        word_encrypted_message = word_encrypted_message.replace(subs,repl)

print(f"The decrypted message is: {word_encrypted_message}")

