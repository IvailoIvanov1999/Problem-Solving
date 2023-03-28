number_cars = int(input())
dict_cars = {}

for _ in range(number_cars):
    cars_input = input().split("|")

    car_drive = cars_input[0]
    mileage = cars_input[1]
    fuel = cars_input[2]
    dict_cars[car_drive] = [mileage, fuel]

while True:
    commands = input().split(" : ")
    action = commands[0]
    if action == "Stop":
        break

    if action == "Drive":
        car_drive = commands[1]
        distance = int(commands[2])
        fuel_drive = int(commands[3])

        if int(dict_cars[car_drive][1]) < fuel_drive:
            print("Not enough fuel to make that ride")
        else:
            curr_distance = int(dict_cars[car_drive][0])
            curr_distance += distance

            curr_fuel = int(dict_cars[car_drive][1])
            curr_fuel -= fuel_drive

            dict_cars[car_drive][0] = curr_distance
            dict_cars[car_drive][1] = curr_fuel

            print(f"{car_drive} driven for {distance} kilometers. {fuel_drive} liters of fuel consumed.")

        if int(dict_cars[car_drive][0]) >= 100000:
            del dict_cars[car_drive]
            print(f"Time to sell the {car_drive}!")

    elif action == "Refuel":
        car_refuel = commands[1]
        fuel_refill = int(commands[2])

        # from_fuel_refill_take = 75 - fuel_refill - max_fuel_capacity_not_over
        max_fuel_capacity_not_over = 75 - int(dict_cars[car_refuel][1])
        result_max_refuel = int(dict_cars[car_refuel][1]) + max_fuel_capacity_not_over

        fuel_refill_result = int(dict_cars[car_refuel][1]) + fuel_refill

        dict_cars[car_refuel][1] = fuel_refill_result
        if int(dict_cars[car_refuel][1]) > 75:
            dict_cars[car_refuel][1] = 75
            print(f"{car_refuel} refueled with {max_fuel_capacity_not_over} liters")
        else:
            print(f"{car_refuel} refueled with {fuel_refill} liters")

    elif action == "Revert":
        car_revert = commands[1]
        kilometres_reverting = int(commands[2])

        result_mileage_on_car = int(dict_cars[car_revert][0]) - kilometres_reverting

        dict_cars[car_revert][0] = result_mileage_on_car

        if int(dict_cars[car_revert][0]) < 10000:
            dict_cars[car_revert][0] = 10000
        else:
            print(f"{car_revert} mileage decreased by {kilometres_reverting} kilometers")

for el in dict_cars:
    print(f"{el} -> Mileage: {dict_cars[el][0]} kms, Fuel in the tank: {dict_cars[el][1]} lt.")
