health = 100
bitcoins = 0
levels = 0
dungeons_rooms = input().split("|")

for el in dungeons_rooms:

    room = el.split()
    command = room[0]
    number = int(room[1])

    if command == "potion":
        last_health = health
        health += number
        levels += 1
        if health >= 100:
            last_health = 100 - last_health
            print(f"You healed for {last_health} hp.")
            health = 100
            print(f"Current health: {health} hp.")
        else:
            print(f"You healed for {number} hp.")
            print(f"Current health: {health} hp.")
    elif command == "chest":
        levels += 1
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        levels +=1
        atack = number
        health -= atack
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {levels}")
            break

        else:
            print(f"You slayed {command}.")


if health > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")


