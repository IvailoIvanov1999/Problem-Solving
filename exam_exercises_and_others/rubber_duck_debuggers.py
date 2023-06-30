from collections import deque

deq_time_programmer = deque([int(x) for x in input().split()])

stack_number_tasks = [int(x) for x in input().split()]

tasks_names_dict = {
    "Darth Vader Ducky": 0,
    "Thor Ducky": 0,
    "Big Blue Rubber Ducky": 0,
    "Small Yellow Rubber Ducky": 0
}

while True:
    if not deq_time_programmer and not stack_number_tasks:
        break

    first_programmer_time = deq_time_programmer.popleft()
    last_task = stack_number_tasks.pop()
    calculation = first_programmer_time * last_task

    if calculation in range(0,60+1):
        tasks_names_dict["Darth Vader Ducky"] += 1
    elif calculation in range(61,120+1):
        tasks_names_dict["Thor Ducky"] += 1
    elif calculation in range(121,180+1):
        tasks_names_dict["Big Blue Rubber Ducky"] += 1
    elif calculation in range(181,240+1):
        tasks_names_dict["Small Yellow Rubber Ducky"] += 1
    elif calculation > 240:
        deq_time_programmer.append(first_programmer_time)
        last_task -= 2
        stack_number_tasks.append(last_task)


print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
for k,v in tasks_names_dict.items():
    print(f"{k}: {v}")
    # print(f"Thor Ducky: {v}")
    # print(f"Big Blue Rubber Ducky: {v}")
    # print(f"Small Yellow Rubber Ducky: {v}")
