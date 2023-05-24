quantity_of_groups = int(input())

all_members = 0

musalla_ppl = 0
monblan_ppl = 0
kilimandjaro_ppl = 0
k2_ppl = 0
everest_ppl = 0

for i in range(quantity_of_groups):
    humans_in_group = int(input())
    all_members = all_members + humans_in_group

    if humans_in_group <= 5:
        musalla_ppl = musalla_ppl + humans_in_group

    elif 6 <=humans_in_group <= 12:
        monblan_ppl = monblan_ppl + humans_in_group

    elif humans_in_group <= 25:
        kilimandjaro_ppl = kilimandjaro_ppl + humans_in_group

    elif 26 <= humans_in_group <= 40:
        k2_ppl = k2_ppl + humans_in_group

    elif humans_in_group >= 41:
        everest_ppl = everest_ppl + humans_in_group

print(f'{(musalla_ppl/all_members)*100:.2f}%')

print(f'{(monblan_ppl/all_members)*100:.2f}%')

print(f'{(kilimandjaro_ppl/all_members)*100:.2f}%')

print(f'{(k2_ppl/all_members)*100:.2f}%')

print(f'{(everest_ppl/all_members)*100:.2f}%')

