days = int(input())
adventurers = int(input())
totalEnergy = float(input())
personWater = float(input())
personFood = float(input())
water_total = 0.0
water_total = float(days * adventurers * personWater)
food_total = 0.0
food_total = float(days * adventurers * personFood)
waterDay = 0
foodDay = 0
for day in range(days):
    wastedEnergy = float(input())
    totalEnergy -= wastedEnergy
    if totalEnergy <= 0.0:
        break
    waterDay += 1
    if waterDay >= 2:
        water_total -= water_total * 0.3
        totalEnergy += totalEnergy * 0.05
        waterDay = 0
    foodDay += 1
    if foodDay >= 3:
        food_total -= (food_total / adventurers)
        totalEnergy += totalEnergy * 0.1
        foodDay = 0

if totalEnergy >= 1:
    print(f"You are ready for the quest. You will be left with - {totalEnergy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_total:.2f}"
          f" food and {water_total:.2f} water.")