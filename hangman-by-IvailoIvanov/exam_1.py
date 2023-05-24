days = int(input())
adventurers = int(input())
energy_total = float(input())
personWater = float(input())
personFood = float(input())
water_total = 0.0
water_total = float(days * adventurers * personWater)
food_total = 0.0
food_total = float(days * adventurers * personFood)
dayly_water = 0
daily_food = 0
for day in range(days):
    energy_waste = float(input())
    energy_total -= energy_waste
    if energy_total <= 0.0:
        break
    dayly_water += 1
    if dayly_water >= 2:
        water_total -= water_total * 0.3
        energy_total += energy_total * 0.05
        dayly_water = 0
    daily_food += 1
    if daily_food >= 3:
        food_total -= (food_total / adventurers)
        energy_total += energy_total * 0.1
        daily_food = 0

if energy_total >= 1:
    print(f"You are ready for the quest. You will be left with - {energy_total:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_total:.2f}"
          f" food and {water_total:.2f} water.")