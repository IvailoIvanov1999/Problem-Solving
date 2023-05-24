string_numbers = input().split(',')

count_of_beggars = int(input())

beggars = [0] * count_of_beggars

for idx in range(len(string_numbers)):
    beggar_idx=idx % count_of_beggars
    num = int(string_numbers[idx])


    beggars[beggar_idx]+=num
print (beggars)