count_of_orders = int(input())
final_price = 0

for _ in range(count_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31 or capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue
    total = (days * capsules_needed_per_day) * price_per_capsule
    final_price += total
    print(f"The price for the coffee is: ${total:.2f}")

    if price_per_capsule < 0.01 or price_per_capsule > 100.00 or days < 1 or days > 31 or capsules_needed_per_day < 1 or capsules_needed_per_day > 2000:
        continue

print(f"Total: ${final_price:.2f}")
