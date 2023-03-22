n = int(input())
heroes_dict = {}
for _ in range(n):
    hero_input = input().split()

    name_hero = hero_input[0]
    hp = hero_input[1]
    mp = hero_input[2]
    heroes_dict[name_hero] = [hp], [mp]

while True:
    comands = input().split(" - ")

    if comands[0] == "End":
        break

    hero = comands[1]

    if comands[0] == "CastSpell":
        # hero = comands[1]
        mp_need = int(comands[2])
        spell_name = comands[3]

        curr_mana = int(''.join(heroes_dict[hero][1]))
        need_to_cast = int(''.join(heroes_dict[hero][1])) - mp_need

        if curr_mana >= mp_need:
            print(
                f"{hero} has successfully cast {spell_name} and now has {need_to_cast} MP!")
            heroes_dict[hero][1].clear()
            heroes_dict[hero][1].append(str(need_to_cast))
        else:
            print(f"{hero} does not have enough MP to cast {spell_name}!")


    elif comands[0] == "TakeDamage":
        # hero = comands[1]
        damage = int(comands[2])
        attacker = comands[3]

        result = int("".join(heroes_dict[hero][0])) - damage
        heroes_dict[hero][0].clear()
        heroes_dict[hero][0].append(str(result))

        if int("".join(heroes_dict[hero][0])) > 0:
            print(f"{hero} was hit for {damage} HP by {attacker} and now has {result} HP left!")
        else:
            del heroes_dict[hero]
            print(f"{hero} has been killed by {attacker}!")

    elif comands[0] == "Recharge":
        # hero = comands[1]
        amount_mana_increase = int(comands[2])

        hero_dict_current_mana = int(''.join(heroes_dict[hero][1]))

        result = hero_dict_current_mana + amount_mana_increase

        if result > 200:
            result = 200
            print(f"{hero} recharged for {result - hero_dict_current_mana} MP!")
        else:
            print(f"{hero} recharged for {amount_mana_increase} MP!")

        heroes_dict[hero][1].clear()
        heroes_dict[hero][1].append(str(result))



    elif comands[0] == "Heal":
        # hero = comands[1]
        amount_heal = int(comands[2])
        current_health_points = int("".join(heroes_dict[hero][0]))

        health_result = current_health_points + amount_heal

        if health_result > 100:
            health_result = 100
            print(f"{hero} healed for {health_result - current_health_points} HP!")
        else:
            print(f"{hero} healed for {amount_heal} HP!")

        heroes_dict[hero][0].clear()
        heroes_dict[hero][0].append(str(health_result))

for k, v in heroes_dict.items():
    print(f"{k}")
    print(f"HP: {''.join(v[0])}")
    print(f"MP: {''.join(v[1])}")
