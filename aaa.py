import re

word = input()

regex = r' ::[A-Z]{1}[a-z]+::|\*+[A-Z]{1}[a-z]+\*+'

result_1 = re.findall(regex, word)

joined = ", ".join(result_1)

result = joined.replace(" ", '')

regex_2 = r"::\[A-Z]{1}[a-z]+::|[A-Z]{1}[a-z]+"

result_2 = re.findall(regex_2, result)

coolness = 0

regex_for_digits = r'\d'

all_digits_in_text = re.findall(regex_for_digits, word)

total_num_sum = 1

for i in all_digits_in_text:
    total_num_sum *= int(i)

print(f"Cool threshold: {total_num_sum}")
print(f"{len(result_2)} emojis found in the text. The cool ones are: ")

splited = result.split(",")

for el in result_2:
    coolness = 0
    for t in range(len(el)):
        check = el[t]
        coolness += ord(el[t])

    if coolness > total_num_sum:
        print(f"{splited[0]}")
        splited.remove(splited[0])
