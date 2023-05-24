# input
month = input()
count_nights = int(input())

# code
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    total_price_apartment = count_nights * apartment
    total_price_studio = count_nights * studio
    if count_nights > 14:
        total_price_studio *= 0.70
    elif count_nights > 7:
        total_price_studio *= 0.95



elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    total_price_apartment = count_nights * apartment
    total_price_studio = count_nights * studio
    if count_nights > 14:
        total_price_studio *= 0.80


elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    total_price_apartment=count_nights * apartment
    total_price_studio=count_nights * studio

if count_nights > 14:
    total_price_apartment*=0.90

# output
print(f"Apartment: {total_price_apartment:.2f} lv.")
print(f"Studio: {total_price_studio:.2f} lv.")

