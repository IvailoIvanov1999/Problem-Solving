type_of_flowers = input()
quantity_of_flowers = int(input())
budget = int(input())

# logic/code


if type_of_flowers == "Roses":
    price = quantity_of_flowers * 5
    if quantity_of_flowers > 80:
        price = price - (price * 0.10)

elif type_of_flowers == "Dahlias":
    price = quantity_of_flowers * 3.80
    if quantity_of_flowers > 90:
        price = price - (price * 0.15)

elif type_of_flowers == "Tulips":
    price = quantity_of_flowers * 2.80
    if quantity_of_flowers > 80:
        price = price-(price* 0.15)

elif type_of_flowers == "Narcissus":
    price = quantity_of_flowers * 3.00
    if quantity_of_flowers < 120:
        price = price+(price * 0.15)

elif type_of_flowers == "Gladiolus":
    price = quantity_of_flowers * 2.50
    if quantity_of_flowers < 80:
        price = price+(price * 0.20)

if budget >= price:
    money_left=budget-price
    print(f'Hey, you have a great garden with {quantity_of_flowers} {type_of_flowers} and {money_left:.2f} leva left.')

else:
    needed_money = price - budget
    print(f"Not enough money, you need {needed_money:.2f} leva more.")
