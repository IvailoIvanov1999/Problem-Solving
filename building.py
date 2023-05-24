count_floors = int(input())

count_rooms = int(input())

counter = 0
flat_name = ""

for f in range(count_floors, 0, -1):
    for r in range(count_rooms):

        counter = f * 10 + r

        if f == count_floors:
            flat_name=f'L{f}{r}'

        elif f % 2 == 0:
            flat_name = f'O{f}{r}'

        elif f % 2 != 0:
            flat_name=f'A{f}{r}'

        print(flat_name,end=" ")

    print()


