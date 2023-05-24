sea_vacation = int(input())

mountain_vacation = int(input())

# sea_vacation_prices = sea_vacation * 680
# mountain_vacation_prices = mountain_vacation * 499

sea_vacation_counter = sea_vacation
mountain_vacation_counter = mountain_vacation
winings = 0

while True:
    type_vacc = input()

    if type_vacc == "sea":
        if sea_vacation_counter == 0:
            continue
        sea_vacation_counter -= 1
        winings = winings + 680

        if sea_vacation_counter < 0:
            sea_vacation_counter = 0


    if type_vacc == "mountain":
        if mountain_vacation_counter== 0:
            continue
        mountain_vacation_counter -= 1
        winings = winings + 499
        if mountain_vacation_counter < 0:
            mountain_vacation_counter = 0


    if sea_vacation_counter == 0 and mountain_vacation_counter == 0:
        print(f'Good job! Everything is sold.')
        print(f'Profit: {winings} leva.')
        break

    if type_vacc == "Stop":
        print(f'Profit: {winings} leva.')
        break