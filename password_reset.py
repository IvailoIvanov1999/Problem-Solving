password = input()

while True:
    command = input()
    command_splited = command.split(" ")

    if command == "Done":
        break

    if command_splited[0] == "TakeOdd":

        password = [password[el] for el in range(len(password)) if el % 2 != 0]
        password = "".join(password)
        print(password)



    elif command_splited[0] == "Cut":

        index = int(command_splited[1])
        length = int(command_splited[2])
        elem_to_cut = password[index:]
        cuted = elem_to_cut[length:]
        password = password[:index] + cuted
        password = "".join(password)
        print(password)



    elif command_splited[0] == "Substitute":
        password = "".join(password)
        substring = command_splited[1]
        substitute = command_splited[2]

        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print("Nothing to replace!")

print(f"Your password is: {password}")
