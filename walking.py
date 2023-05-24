goal_steps_per_day = 10000

total_steps_counter = 0

steps_count_every_day = input()
while steps_count_every_day != "Going home":
    steps = int(steps_count_every_day)

    total_steps_counter = steps + total_steps_counter

    if total_steps_counter >= goal_steps_per_day:
        break

    steps_count_every_day = input()

if steps_count_every_day == "Going home":
    steps_walked = int(input())
    total_steps_counter = steps_walked + total_steps_counter

diff = abs(goal_steps_per_day - total_steps_counter)

if total_steps_counter >= goal_steps_per_day:

    print(f'Goal reached! Good job!')
    print(f"{diff} steps over the goal!")

else:
    print(f"{diff} more steps to reach goal.")
