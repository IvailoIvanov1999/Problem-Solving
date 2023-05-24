from collections import deque

deque_elf_energy = deque(int(x) for x in input().split())

stack_materials_in_box = [int(x) for x in input().split()]

toys_made = 0

counter_times = 0

curr_elf_making = 0

total_used_energy = 0

while True:

    if not deque_elf_energy:
        break
    if not stack_materials_in_box:
        break

    # first elf
    first_elf_energy = deque_elf_energy[0]
    if first_elf_energy < 5:
        deque_elf_energy.popleft()
        continue
    # last box
    last_box_materials = stack_materials_in_box[-1]

    counter_times += 1

    if counter_times == 3:
        if first_elf_energy >= last_box_materials * 2:
            total_used_energy += last_box_materials
            curr_elf_making += 2
            deque_elf_energy[0] += 1
            elf_to_go_to_end_of_que = deque_elf_energy.popleft()
            deque_elf_energy.append(elf_to_go_to_end_of_que)
            stack_materials_in_box.pop()
        else:
            elf_to_go_to_end_of_que = 2 * deque_elf_energy.popleft()
            deque_elf_energy.append(elf_to_go_to_end_of_que)
            continue

    if counter_times == 5:
        counter_times = 0
        if first_elf_energy >= last_box_materials:
            total_used_energy += last_box_materials
            deque_elf_energy[0] -= last_box_materials
            curr_elf_making += 1

        else:
            elf_to_go_to_end_of_que = 2 * deque_elf_energy.popleft()
            deque_elf_energy.append(elf_to_go_to_end_of_que)
            continue

        if curr_elf_making == 2:
            curr_elf_making = 0



    elif first_elf_energy >= last_box_materials:
        deque_elf_energy[0] -= last_box_materials
        total_used_energy += last_box_materials
        deque_elf_energy[0] += 1
        elf_to_go_to_end_of_que = deque_elf_energy.popleft()
        deque_elf_energy.append(elf_to_go_to_end_of_que)
        stack_materials_in_box.pop()

        curr_elf_making += 1
    else:
        elf_to_go_to_end_of_que = 2 * deque_elf_energy.popleft()
        deque_elf_energy.append(elf_to_go_to_end_of_que)

    toys_made += curr_elf_making

    curr_elf_making = 0

print(f"Toys: {toys_made}")
print(f"Energy: {total_used_energy}")
if deque_elf_energy:
    print(f"Elves left: {', '.join([str(x) for x in deque_elf_energy])}", )

if stack_materials_in_box:
    print(f"Boxes left: {', '.join([str(x) for x in stack_materials_in_box])}")
