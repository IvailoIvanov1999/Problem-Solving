spell = input()
list_actions = ["Abjuration", "Necromancy", "Illusion", "Divination", "Alteration"]
while True:
    command = input().split(" ")
    action = command[0]

    if action == "Abracadabra":
        break

    if action not in list_actions:
        print("The spell did not work!")

    elif action == "Abjuration":
        spell = spell.upper()
        print(spell)


    elif action == "Necromancy":
        spell = spell.lower()
        print(spell)


    elif action == "Illusion":
        ill_index = int(command[1])
        ill_letter = command[2]
        if ill_index < 0 or ill_index >= (len(spell)):
            print("The spell was too weak.")
        else:
            spell = spell[:ill_index] + ill_letter + spell[ill_index+1:]
            print("Done!")


    elif action == "Divination":
        f_subs = command[1]
        s_subs = command[2]
        if f_subs not in spell:
            continue
        else:
            spell = spell.replace(f_subs, s_subs)
            print(spell)


    elif action == "Alteration":
        subs_to_remove = command[1]

        if subs_to_remove not in spell:
            continue
        else:
            spell = spell.replace(subs_to_remove, "")
            print(spell)
