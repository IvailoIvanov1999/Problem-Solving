budget = int(input())
comand=input()
total_price=0

while comand != "End":
    prices = int(comand)

    total_price+=prices

    if total_price > budget:
        print("You went in overdraft!")
        break
    comand=input()
else:
    print('You bought everything needed.')

