rows, cols = tuple(map(int, input().split(', ')))
matrix = []
symbols = 0
collected_symbols = 0
end_of_program = False

for row in range(rows):
    matrix.append(input().split())
    if "Y" in matrix[row]:
        current_position = [row, matrix[row].index("Y")]


for r in range(rows):
    for c in range(cols):
        if matrix[r][c] == "D" or matrix[r][c] == "G" or matrix[r][c] == "C":
            symbols += 1

my_dict = {"Christmas decorations": 0, "Gifts": 0, "Cookies": 0}

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while True:
    command = input()
    if command == "End":
        break

    command = command.split('-')
    direction = command[0]
    steps = int(command[1])

    while steps != 0:
        new_row = current_position[0] + directions[direction][0]
        new_col = current_position[1] + directions[direction][1]

        if new_row < 0:
            new_row = rows - 1
        elif new_row > rows - 1:
            new_row = 0

        if new_col < 0:
            new_col = cols - 1
        elif new_col > cols - 1:
            new_col = 0

        matrix[current_position[0]][current_position[1]] = "x"
        current_position = [new_row, new_col]
        if matrix[current_position[0]][current_position[1]] == "D":
            my_dict["Christmas decorations"] += 1
            collected_symbols += 1
        elif matrix[current_position[0]][current_position[1]] == "G":
            my_dict["Gifts"] += 1
            collected_symbols += 1
        elif matrix[current_position[0]][current_position[1]] == "C":
            my_dict["Cookies"] += 1
            collected_symbols += 1

        matrix[current_position[0]][current_position[1]] = "Y"
        steps -= 1

        if collected_symbols == symbols:
            end_of_program = True
            break
    if end_of_program:
        break

if end_of_program:
    print("Merry Christmas!")

print("You've collected:")
for k, v in my_dict.items():
    print(f"- {v} {k}")

for row in matrix:
    print(*row)