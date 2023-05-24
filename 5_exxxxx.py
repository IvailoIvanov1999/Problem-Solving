sea_count = int(input())
mountain_count = int(input())
sea_cost = 680
mountain_cost = 499
profit_sum = 0
while True:
    package_name = input()
    if package_name == "Stop":
        break
    if package_name == "sea":
        if sea_count == 0:
            continue
        profit_sum += sea_cost
        sea_count -= 1
    if package_name == "mountain":
        if mountain_count == 0:
            continue
        profit_sum += mountain_cost
        mountain_count -= 1
    if sea_count == 0 and mountain_count == 0:
        print("Good job! Everything is sold.")
        break
print(f"Profit: {profit_sum} leva.")
