budget = float(input())
season = input()

# code
final_budget = 0
if budget <= 100:
    if season == "summer":
        final_budget = budget * 0.70
    elif season == "winter":
        final_budget = budget * 0.30
    place = "Bulgaria"

elif budget <= 1000:
    if season == "summer":
        final_budget = budget * 0.60
    elif season == "winter":
        final_budget = budget * 0.20
    place = "Balkans"

elif budget > 1000:
    final_budget = budget * 0.10
    place = "Europe"

if place=="Europe":
    where="Hotel"
elif season == "summer":
    where = "Camp"
elif season == "winter":
    where = "Hotel"


final_price = budget - final_budget

print(f"Somewhere in {place}")
print(f"{where} - {final_price:.2f}")
