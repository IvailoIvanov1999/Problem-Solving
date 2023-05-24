destination = input()

saved_money = 0
# desired_dest = " "

while destination != "End":
    minimal_budget = float(input())

    while saved_money <= minimal_budget:
        saving_money = float(input())

        saved_money = saved_money + saving_money

        if saved_money >= minimal_budget:
            print(f"Going to {destination}!")
            break

    saved_money = 0

    destination = input()
