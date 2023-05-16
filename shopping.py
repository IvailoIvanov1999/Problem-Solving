budget_petur = float(input())
videocards = int(input())
procecors = int(input())
ram = int(input())

videocards_price = videocards * 250

procecors_price = procecors * (videocards_price * 0.35)

ram_price = ram * (videocards_price * 0.10)

total_prices = videocards_price + procecors_price + ram_price

if videocards > procecors:
    total_prices_discount = total_prices * 0.15
    total_prices = total_prices - total_prices_discount

if budget_petur >= total_prices:
    budget_left = budget_petur - total_prices
    print(f"You have {budget_left:.2f} leva left!")

elif budget_petur < total_prices:
    needed_money = total_prices - budget_petur
    print(f"Not enough money! You need {needed_money:.2f} leva more!")
