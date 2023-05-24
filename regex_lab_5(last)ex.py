import re



group_list = []

total_money_spend = 0

while True:
    word = input()
    if word == "Purchase":
        break
    # regex = r">>([A-Za-z]+)<<(\d+|\d\.+)!(\d+)"
    regex = r"^>>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"

    formatedd_word = re.findall(regex, word)
    if not formatedd_word:
        continue

    group = formatedd_word[0]

    item = group[0]
    value = float(group[1])
    quantity = int(group[2])

    total_money_spend += value * quantity
    group_list.append(item)



# for el in result:
#     key = el[0]
#     if "." in el[1]:
#         value = float(el[1]) * int(el[2])
#     else:
#         value = int(el[1]) * int(el[2])
#
#     dict_result[key] = value
#
#     total_money_spend += value


print(f'Bought furniture:')

for itemsss in group_list:
    print(itemsss)

print(f"Total money spend: {total_money_spend:.2f}")
