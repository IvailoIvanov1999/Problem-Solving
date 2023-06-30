from collections import deque

stack_milligrams_coffeine_input = [int(x) for x in input().split(", ")]
energy_drinks = deque([int(x) for x in input().split(", ")])

coffeine_taken = 0

while stack_milligrams_coffeine_input and energy_drinks:


    last_mlgr_coffeine = stack_milligrams_coffeine_input.pop()
    first_energy_drink = energy_drinks.popleft()
    calculation_caffeine_in_current_drink = last_mlgr_coffeine * first_energy_drink

    if coffeine_taken + calculation_caffeine_in_current_drink <= 300:
        coffeine_taken += calculation_caffeine_in_current_drink
    else:
        energy_drinks.append(first_energy_drink)
        coffeine_taken -= 30
        if coffeine_taken < 0:
            coffeine_taken = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {coffeine_taken} mg caffeine.")
