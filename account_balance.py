counter_money = 0
while True:
    money = input()

    if money == "NoMoreMoney":
        break

    money = float(money)

    if money > 0:
        counter_money += money
        print(f'Increase: {money:.2f}')

    else:
        print("Invalid operation!")
        break

print(f'Total: {counter_money:.2f}')
