import re

word = input()

# regex = r'::([A-Z][a-z]{2,})::|\*\*([A-Z][a-z]{2,})\*\*'
regex = r'(::[A-Z][a-z]{2,}::)|(\*\*[A-Z][a-z]{2,}\*\*)'

result_1 = re.findall(regex, word)

coolness = 0

regex_for_digits = r'\d'

all_digits_in_text = re.findall(regex_for_digits, word)

total_num_sum = 1

for i in all_digits_in_text:
    total_num_sum *= int(i)

print(f"Cool threshold: {total_num_sum}")
print(f"{len(result_1)} emojis found in the text. The cool ones are: ")

for el in result_1:
    coolness = 0
    if "" in el:
        el = "".join(el)
    for t in range(2,len(el)-2):
        want=el[t]
        coolness += ord(el[t])

    if coolness > total_num_sum:
        print(f"{el}")

