price_for_baggage_over_20kg = float(input())

kilograms_baggage = float(input())

days_until_travel = int(input())

quantity_baggages = int(input())

# kilos price
baggage_price = 0

if kilograms_baggage < 10:
    baggage_price = price_for_baggage_over_20kg - (price_for_baggage_over_20kg-(price_for_baggage_over_20kg * (20/100)))

elif 10 <= kilograms_baggage <= 20:
    baggage_price = price_for_baggage_over_20kg * 0.50

elif kilograms_baggage > 20:
    baggage_price = price_for_baggage_over_20kg

# days number meaning
if days_until_travel > 30:
    baggage_price = baggage_price + (baggage_price * (10 / 100))

elif 7 <= days_until_travel <= 30:
    baggage_price = baggage_price + (baggage_price * 0.15)

elif days_until_travel < 7:
    baggage_price = baggage_price + (baggage_price * 0.40)

final_baggage_price = quantity_baggages * baggage_price

print(f"The total price of bags is: {final_baggage_price:.2f} lv. ")
