import math

coins = float(input())

coins = math.floor(coins * 100)
coins_counter = 0
while coins > 0:

    if coins >= 200:
        coins = coins - 200

    elif coins >= 100:
        coins = coins - 100

    elif coins >= 50:
        coins = coins - 50

    elif coins >= 20:
        coins = coins - 20
    elif coins >= 10:
        coins = coins - 10

    elif coins >= 5:
        coins = coins - 5

    elif coins >= 2:
        coins = coins - 2

    elif coins >= 1:
        coins = coins - 1

    else:
        break
    coins_counter += 1

print(coins_counter)
