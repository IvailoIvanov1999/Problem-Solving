plants = {}

n = int(input())
for i in range(n):
    plant_info = input().split("<->")
    plant = plant_info[0]
    rarity = int(plant_info[1])
    plants[plant] = {"rarity": rarity, "ratings": []}

command = input()
while command != "Exhibition":
    tokens = command.split()
    if tokens[0] == "Rate:":
        plant = tokens[1]
        if plant in plants:
            rating = int(tokens[3])
            plants[plant]["ratings"].append(rating)
        else:
            print("error")
    elif tokens[0] == "Update:":
        plant = tokens[1]
        if plant in plants:
            rarity = int(tokens[3])
            plants[plant]["rarity"] = rarity
        else:
            print("error")
    elif tokens[0] == "Reset:":
        plant = tokens[1]
        if plant in plants:
            plants[plant]["ratings"] = []
        else:
            print("error")
    else:
        print("error")
    command = input()

print("Plants for the exhibition:")
for plant, info in plants.items():
    if info["ratings"]:
        avg_rating = sum(info["ratings"]) / len(info["ratings"])
        avg_rating = f'{avg_rating:.2f}'
    else:
        avg_rating = f"0.00"
    print(f"- {plant}; Rarity: {info['rarity']}; Rating: {avg_rating}")