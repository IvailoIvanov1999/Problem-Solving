from collections import deque

deq_f_efects = deque([int(x) for x in input().split(", ")])

stack_explosive_power = [int(x) for x in input().split(", ")]

palm_firework = 0
willow_firework = 0
crossette_firework = 0

while deq_f_efects and stack_explosive_power:
    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        break
    first_firework = deq_f_efects.popleft()
    last_explosive_power = stack_explosive_power.pop()
    if first_firework <= 0 and last_explosive_power <= 0:
        continue
    if first_firework <= 0:
        stack_explosive_power.append(last_explosive_power)
        continue

    if last_explosive_power <= 0:
        deq_f_efects.appendleft(first_firework)
        continue

    sum_values = first_firework + last_explosive_power
    if sum_values % 3 == 0 and sum_values % 5 == 0:
        crossette_firework += 1
    elif sum_values % 5 == 0 and sum_values % 3 != 0:
        willow_firework += 1
    elif sum_values % 3 == 0 and sum_values % 5 != 0:
        palm_firework += 1

    else:
        first_firework -= 1
        deq_f_efects.append(first_firework)
        stack_explosive_power.append(last_explosive_power)

if palm_firework and willow_firework and crossette_firework >= 3:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if deq_f_efects:
    print(f"Firework Effects left: {', '.join([str(x) for x in deq_f_efects])}")

if stack_explosive_power:
    print(f'Explosive Power left: {", ".join([str(x) for x in stack_explosive_power])}')

print(f"Palm Fireworks: {palm_firework}")
print(f"Willow Fireworks: {willow_firework}")
print(f"Crossette Fireworks: {crossette_firework}")
