from collections import deque

size = int(input())

commands = deque(input().split(', '))

navigations = [
    # up
    (-1, 0),
    # down
    (+1, 0),
    # left
    (0, -1),
    # right
    (0, +1)
]


def moves(c, rows, cols):
    squirrel_starting_row = rows
    squirrel_starting_col = cols

    if c == "up":
        squirrel_starting_row += navigations[0][0]
        squirrel_starting_col += navigations[0][1]

    if c == "down":
        squirrel_starting_row += navigations[1][0]
        squirrel_starting_col += navigations[1][1]

    if c == "left":
        squirrel_starting_row += navigations[2][0]
        squirrel_starting_col += navigations[2][1]

    if c == "right":
        squirrel_starting_row += navigations[3][0]
        squirrel_starting_col += navigations[3][1]

    return squirrel_starting_row, squirrel_starting_col


hazelnuts = 0

hazelnuts_quest_completed = False
trap_found = False
out_of_matrix = False

matrix = [[x for x in input()] for _ in range(size)]

squirrel_starting_row = 0
squirrel_starting_col = 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == "s":
            squirrel_starting_row, squirrel_starting_col = row, col

matrix[squirrel_starting_row][squirrel_starting_col] = "*"

while True:
    if not commands:
        break
    command_income = commands.popleft()
    squirrel_starting_row, squirrel_starting_col = moves(command_income, squirrel_starting_row, squirrel_starting_col)
    a = 0 <= squirrel_starting_row < size
    b = 0 <= squirrel_starting_col < size
    if not (a and b):
        out_of_matrix = True
        break

    if hazelnuts_quest_completed or trap_found or out_of_matrix:
        break

    elif matrix[squirrel_starting_row][squirrel_starting_col] == "h":
        hazelnuts += 1
        if hazelnuts >= 3:
            hazelnuts_quest_completed = True
            break
        matrix[squirrel_starting_row][squirrel_starting_col] = "*"

    elif matrix[squirrel_starting_row][squirrel_starting_col] == "t":
        trap_found = True
        break

if out_of_matrix:
    print("The squirrel is out of the field.")
    print(f"Hazelnuts collected: {hazelnuts}")
elif trap_found:
    print("Unfortunately, the squirrel stepped on a trap...")
    print(f"Hazelnuts collected: {hazelnuts}")
elif hazelnuts_quest_completed:
    print("Good job! You have collected all hazelnuts!")
    print(f"Hazelnuts collected: {hazelnuts}")
else:
    print("There are more hazelnuts to collect.")
    print(f"Hazelnuts collected: {hazelnuts}")
