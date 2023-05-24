days = int(input())

plunder_for_day = int(input())

expected_plunder = float(input())

days_counter = 1

total_plundered = 0

for _ in range(days):
    total_plundered += plunder_for_day

    if days_counter % 3 == 0:
        more_gain = plunder_for_day * 0.50
        total_plundered += more_gain

    elif days_counter % 5 == 0:
        lose_plunder = total_plundered * 0.30
        total_plundered -= lose_plunder
    days_counter += 1

if total_plundered >= expected_plunder:
    print(f"Ahoy! {total_plundered:.2f} plunder gained.")

elif total_plundered < expected_plunder:

    percent = total_plundered * 100 / expected_plunder
    print(f"Collected only {percent:.2f}% of the plunder.")
