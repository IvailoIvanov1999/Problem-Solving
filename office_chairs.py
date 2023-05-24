number_of_rooms = int(input())

chairs_left = 0
chairs_need = 0

counter_rooms = 0
total_chairs, total_visitors = 0, 0
for _ in range(number_of_rooms):
    chairs, visitors = input().split()
    counter_rooms += 1

    visitors = int(visitors)

    total_chairs = len(chairs)
    total_visitors = visitors
    chairs_left += total_chairs - total_visitors

    chairs_need = abs(len(chairs) - visitors)

    if len(chairs) < visitors:
        print(f"{chairs_need} more chairs needed in room {counter_rooms}")

if chairs_left >= visitors or chairs_left == 0:
    print(f"Game On, {chairs_left} free chairs left")
