import re
new_list = []
travel_points = 0
word = input()

pattern = r"=([A-Z]{1}[A-Za-z]{2,})=|\/([A-Z]{1}[A-Za-z]{2,})\/"

regex = re.findall(pattern, word)

for items in regex:
    item_as_list = [*items]

    if "" in item_as_list:
        item_as_list.remove("")
        new_list.append(*item_as_list)

for i in range(len(new_list)):
    travel_points += len(new_list[i])


print(f"Destinations: {', '.join(new_list)}")
print(f"Travel Points: {travel_points}")
