status_pirate_ship = [int(x) for x in input().split(">")]

warship = [int(x) for x in input().split(">")]

max_health_capacity = int(input())

while True:
    comandddd = input().split()

    move = comandddd[0]

    if move == "Retire":
        break

    if move == "Fire":
        indexx = int(comandddd[1])
        damage = int(comandddd[2])
        if indexx >= 0 and indexx < len(warship):
            warship[indexx] -= damage
            if warship[indexx] <= 0:
                print("You won! The enemy ship has sunken.")
                exit()
        else:
            continue

    elif move == "Defend":
        index_start = int(comandddd[1])
        end_index = int(comandddd[2])
        damage = int(comandddd[3])
        if index_start >= 0 and index_start < len(status_pirate_ship) and end_index >= 0 and end_index < len(
                status_pirate_ship):
            for idx in range(index_start, end_index + 1):
                status_pirate_ship[idx] -= damage
            if status_pirate_ship[idx] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()

    elif move == "Repair":
        indexxx = int(comandddd[1])
        healthhhh = int(comandddd[2])
        if indexxx >= 0 and indexxx < len(status_pirate_ship):
            status_pirate_ship[indexxx] += healthhhh
            if status_pirate_ship[indexxx] > max_health_capacity:
                status_pirate_ship[indexxx] = max_health_capacity
        else:
            continue
    elif move == "Status":

        sections_problem = max_health_capacity * 0.20

        counter = len([x for x in status_pirate_ship if x < sections_problem])

        print(f'{counter} sections need repair.')


print(f"Pirate ship status: {sum(status_pirate_ship)}")
print(f"Warship status: {sum(warship)}")
