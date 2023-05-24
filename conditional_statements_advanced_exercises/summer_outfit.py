degrees = int(input())
time_from_day = input()

# code
if 10 <= degrees <= 18:
    if time_from_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif time_from_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_from_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if 18 < degrees <= 24:
    if time_from_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
    elif time_from_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_from_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")

if degrees >= 25:
    if time_from_day=="Morning":
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif time_from_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
    elif time_from_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"

    print(f"It's {degrees} degrees, get your {outfit} and {shoes}.")
