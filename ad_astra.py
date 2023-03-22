import re
list_all = []

calories_all_food = 0
text_string = input()

pattern = r'\|([A-Za-z ]+)\|(\d{2}\/\d{2}\/\d{2})\|(\d+)\||#([A-Za-z ]+)#(\d{2}\/\d{2}\/\d{2})#(\d+)#'

regex_word = re.findall(pattern, text_string)

for items in regex_word:

    list_item = [*items]
    for _ in range(len(list_item)):
        if "" in list_item:
            list_item.remove("")

    item = list_item[0]
    dates = list_item[1]
    calories = int(list_item[2])
    listtt = [item,dates,calories]
    list_all.append(listtt)

    calories_all_food += calories

days_i_can_last_with_this_food = calories_all_food // 2000

print(f"You have food to last you for: {days_i_can_last_with_this_food} days!")

for i in range(len(list_all)):
    if len(list_all) == 0:
        break
    print(f"Item: {list_all[i][0]}, Best before: {list_all[i][1]}, Nutrition: {list_all[i][2]}")




