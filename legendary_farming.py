spec_materials = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}
junk = {}
flag = False
while True:
    line = input()
    data = line.split()

    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1].lower()

        if material in spec_materials:
            spec_materials[material] += quantity
            if spec_materials[material] >= 250:
                flag = True
                break
        else:
            if material in junk:

                junk[material] += quantity
            else:
                junk[material] = quantity

    if flag:
        break

if spec_materials["fragments"] >= 250:
    spec_materials["fragments"] -= 250
    item_obtained = "Valanyr"

elif spec_materials["shards"] >= 250:
    spec_materials["shards"] -= 250
    item_obtained = "Shadowmourne"

elif spec_materials["motes"] >= 250:
    spec_materials["motes"] -= 250
    item_obtained = "Dragonwrath"

print(f"{item_obtained} obtained!")
print(f"shards: {spec_materials['shards']}\n"
      f"fragments: {spec_materials['fragments']}\n"
      f"motes: {spec_materials['motes']}")
for key, value in junk.items():
    print(f"{key}: {value}")























































































































































































































