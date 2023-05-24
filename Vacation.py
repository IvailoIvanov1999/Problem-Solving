needed_money_for_vacation = float(input())
money_she_has = float(input())

days_counter = 0
# spending money
spent_money = 0
days_spending = 0
total_money = money_she_has

# save money
saving_money = 0
total_saved_money = 0
#

while total_money < needed_money_for_vacation :
    if days_spending >= 5:
        break

    spend_or_save = input()
    money_she_saved_or_spent = float(input())

    days_counter += 1

    if spend_or_save == "spend":
        days_spending = days_spending + 1
        total_money = total_money - money_she_saved_or_spent
        if total_money < 0:
            total_money = 0

    elif spend_or_save == "save":
        days_spending = 0
        total_money = total_money + money_she_saved_or_spent

if days_spending == 5:
    print(f"You can't save the money.")
    print(f"{days_counter}")

elif total_money >= needed_money_for_vacation:
    print(f"You saved the money for {days_counter} days.")
