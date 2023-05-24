word_input = input().split()

str_1 = word_input[0]
str_2 = word_input[1]

str_1_sum = []
str_2_sum = []

total_calc = 0

character_counter_1 = 0
character_counter_2 = 0

min_lenght = min(len(str_1),len(str_2))


if len(str_1) > len(str_2):
    diference_str1_len = len(str_1) - len(str_2)
    new_str_1 = str_1[::-1]
    for i_1 in range(diference_str1_len):
        total_calc += ord(new_str_1[0])
        list_str1 = [chhh for chhh in new_str_1]
        list_str1.remove(list_str1[0])
        str_1 = "".join(list_str1[::-1])

elif len(str_1) < len(str_2):
    diference_str2_len = len(str_2) - len(str_1)
    new_str_2 = str_2[::-1]
    for i_1 in range(diference_str2_len):
        total_calc += ord(new_str_2[0])
        list_str2 = [chhh2 for chhh2 in new_str_2]
        list_str2.remove(list_str2[0])
        str_1 = "".join(list_str2[::-1])


for ch in str_1:
    str_1_sum.append(ord(ch))
    character_counter_1 += 1

for ch2 in str_2:
    str_2_sum.append(ord(ch2))
    character_counter_2 += 1

for t in range(character_counter_1 + character_counter_2):
    total_calc += str_1_sum[0] * str_2_sum[0]
    str_1_sum.remove(str_1_sum[0])
    str_2_sum.remove(str_2_sum[0])
    if len(str_1_sum) == 0:
        break


print(total_calc)
