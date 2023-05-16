budget_film = float(input())
statists_number = int(input())
price_clothes_per_statist = float(input())

# decor_for_film
decor = budget_film * 0.10

clothes_all_money = statists_number * price_clothes_per_statist

decor_and_clothes=decor + clothes_all_money

# clothes_discount

if statists_number > 150:
    clothes_discount = clothes_all_money * 0.10
    total_clothes_price = clothes_all_money - clothes_discount
    decor_and_clothes = decor + total_clothes_price

if decor_and_clothes > budget_film:
    needed_money =decor_and_clothes- budget_film
    print("Not enough money!")
    print(f"Wingard needs {needed_money:.2f} leva more.")

else:
    decor_and_clothes <= budget_film
    money_left = budget_film - decor_and_clothes
    print("Action!")
    print(f'Wingard starts filming with {money_left:.2f} leva left.')
