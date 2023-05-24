lily_age = int(input())
price_washmachine = float(input())
toy_price = int(input())

birthday_money_savings = 0
toys_count = 0
total_money = 0
brother_stealings = 0

for i in range(1, lily_age + 1):
    if i % 2 == 0:
        birthday_money_savings = birthday_money_savings + 10
        total_money = total_money + birthday_money_savings
        brother_stealings = brother_stealings + 1

    else:
        toys_count += 1

money_from_toys = toy_price * toys_count

all_money_lily=(total_money+money_from_toys)-brother_stealings

if all_money_lily >=price_washmachine:
    money_left=abs(all_money_lily-price_washmachine)
    print(f'Yes! {money_left:.2f}')
else:
    diff=abs(all_money_lily-price_washmachine)
    print(f"No! {diff:.2f}")
