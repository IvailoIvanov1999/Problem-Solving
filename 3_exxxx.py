dancers = int(input())

points = float(input())

season = input()

place = input('vuvedete mqsto : ')

if place == "Bulgaria":
    money_won = points * dancers
    discount = 0

    if season == "summer":
        money_won = money_won * 0.95

    if season == "winter":
        money_won = money_won - (money_won * 0.08)






elif place == "Abroad":
    money_won = (dancers * points)
    money_won = money_won + (money_won * 0.50)

    if season == "summer":
        money_won = money_won * 0.90

    if season == "winter":
        money_won = money_won * 0.85



donate_sum = money_won - (money_won * 0.25)
total = money_won - donate_sum
players_received = total / dancers

print(f'Charity - {donate_sum:.2f}')
print(f'Money per dancer - {players_received:.2f}')
