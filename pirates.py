dict_pirates = {}
while True:
    input_first_line = input().split("||")

    if input_first_line[0] == "Sail":
        break

    city = input_first_line[0]
    if city in dict_pirates:
        population = input_first_line[1]
        gold = input_first_line[2]

        # Population calculation
        dict_pirates[city][0] .append(population)
        popul = str(sum([int(x) for x in dict_pirates[city][0]]))
        dict_pirates[city][0] = [popul]

        # Gold calculations
        dict_pirates[city][1] .append(gold)
        golddd = str(sum([int(z) for z in dict_pirates[city][1]]))
        dict_pirates[city][1] = [golddd]
    else:
        population = input_first_line[1]
        gold = input_first_line[2]
        dict_pirates[city] = [[population], [gold]]

while True:
    comands = input().split("=>")

    if comands[0] == "End":
        break

    move = comands[0]

    if move == "Plunder":
        cityy_to_plund = comands[1]
        people = comands[2]
        gold_plunder = comands[3]

        result_people = int("".join(dict_pirates[cityy_to_plund][0])) - int(people)
        dict_pirates[cityy_to_plund][0] = [str(result_people)]

        result_gold = int("".join(dict_pirates[cityy_to_plund][1])) - int(gold_plunder)
        dict_pirates[cityy_to_plund][1] = [str(result_gold)]
        print(f"{cityy_to_plund} plundered! {gold_plunder} gold stolen, {people} citizens killed.")
        curr_people = ''.join(dict_pirates[cityy_to_plund][0])
        curr_gold = ''.join(dict_pirates[cityy_to_plund][1])
        if curr_people == '0' or curr_gold == '0':
            del dict_pirates[cityy_to_plund]
            print(f"{cityy_to_plund} has been wiped off the map!")

    elif move == "Prosper":
        city_grow = comands[1]
        gold_to_grow = int(comands[2])
        if gold_to_grow < 0:
            print("Gold added cannot be a negative number!")
            continue
        else:
            gold_in_town = sum([int(x) for x in dict_pirates[city_grow][1]]) + gold_to_grow
            dict_pirates[city_grow][1].clear()
            dict_pirates[city_grow][1].append(str(gold_in_town))
            print(f"{gold_to_grow} gold added to the city treasury. {city_grow} now has {gold_in_town} gold.")

if len(dict_pirates) > 0:
    print(f"Ahoy, Captain! There are {len(dict_pirates)} wealthy settlements to go to:")
    for el in dict_pirates:
        print(f"{el} -> Population: {''.join(dict_pirates[el][0])} citizens, Gold: {''.join(dict_pirates[el][1])} kg)")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
