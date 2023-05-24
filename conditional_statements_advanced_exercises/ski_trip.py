# input
days_to_stay = int(input())
type_of_room = input()
rate = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35

# code
total_price_for_one_person = (days_to_stay-1) * room_for_one_person
total_price_apartment = (days_to_stay-1) * apartment
total_price_president_apartment = (days_to_stay-1) * president_apartment

if days_to_stay < 10:

    if type_of_room == "apartment" or type_of_room == "president apartment"or type_of_room=="room for one person":
        final_ap = total_price_apartment * 0.70
        final_pr_ap = total_price_president_apartment * 0.90
        total_price_for_one_person=total_price_for_one_person

elif 10 <= days_to_stay <= 15 :

    if type_of_room == "apartment"or type_of_room == "president apartment"or type_of_room=="room for one person":
        final_ap = total_price_apartment * 0.65
        final_pr_ap = total_price_president_apartment * 0.85
        total_price_for_one_person=total_price_for_one_person

elif days_to_stay > 15:

    if type_of_room == "apartment" or type_of_room == "president apartment"or type_of_room=="room for one person":
        final_ap = total_price_apartment * 0.50
        final_pr_ap = total_price_president_apartment * 0.80
        total_price_for_one_person=total_price_for_one_person

if rate == "positive":
    final_ap+=(final_ap*0.25)
    total_price_for_one_person+=(total_price_for_one_person*0.25)
    final_pr_ap+=(final_pr_ap*0.25)

elif rate=="negative":
    final_ap=final_ap-(final_ap*0.10)
    total_price_for_one_person=total_price_for_one_person-(total_price_for_one_person*0.10)
    final_pr_ap=final_pr_ap - (final_pr_ap*0.10)

if type_of_room=="room for one person":
    print(f'{total_price_for_one_person:.2f}')

elif type_of_room=="apartment":
    print(f'{final_ap:.2f}')

elif type_of_room=="president apartment":
    print(f'{final_pr_ap:.2f}')