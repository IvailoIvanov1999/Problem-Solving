from collections import deque

seats = input().split(', ')

first_sequence_que = deque([int(x) for x in input().split(', ')])
second_sequence_stack = [int(x) for x in input().split(', ')]
already_taken_seats = []
rotations = 0
found_seats_count = 0
while True:
    if rotations >= 10:
        break
    if found_seats_count >= 3:
        break
    first_number = first_sequence_que.popleft()
    last_number = second_sequence_stack.pop()
    the_sum = first_number + last_number

    char_ascii = chr(the_sum)

    first_num_plus_char = str(first_number) + char_ascii
    second_num_plus_char = str(last_number) + char_ascii
    rotations += 1



    if first_num_plus_char in seats or second_num_plus_char in seats:
        if first_num_plus_char in already_taken_seats or second_num_plus_char in already_taken_seats:
            continue
        else:
            if first_num_plus_char in seats:
                found_seats_count += 1
                seats.remove(first_num_plus_char)
                already_taken_seats.append(first_num_plus_char)
            if second_num_plus_char in seats:
                found_seats_count += 1
                seats.remove(second_num_plus_char)
                already_taken_seats.append(second_num_plus_char)

    else:
        first_sequence_que.append(first_number)
        second_sequence_stack.insert(0, last_number)

print(f"Seat matches: {', '.join([x for x in already_taken_seats])}")
print(f"Rotations count: {rotations}")
