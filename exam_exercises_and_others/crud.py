matrix = [[x for x in input().split()] for _ in range(6)]

first_cords = input()

start_position_row, start_position_col = int(first_cords[1]), int(first_cords[4])

dict_directions = {
    'left': (0, -1),
    'right': (0, +1),
    'up': (-1, 0),
    'down': (+1, 0)
}

while True:
    command = input().split(", ")
    type_ = command[0]
    if type_ == "Stop":
        break

    direction = command[1]

    if type_ == "Create":
        value_ = command[2]
        start_position_row += dict_directions[direction][0]
        start_position_col += dict_directions[direction][1]
        if matrix[start_position_row][start_position_col] == ".":
            matrix[start_position_row][start_position_col] = value_

    elif type_ == 'Update':
        value_ = command[2]
        start_position_row += dict_directions[direction][0]
        start_position_col += dict_directions[direction][1]
        if matrix[start_position_row][start_position_col] != ".":
            matrix[start_position_row][start_position_col] = value_

    elif type_ == 'Delete':
        start_position_row += dict_directions[direction][0]
        start_position_col += dict_directions[direction][1]
        if matrix[start_position_row][start_position_col] != ".":
            matrix[start_position_row][start_position_col] = "."

    elif type_ == 'Read':
        start_position_row += dict_directions[direction][0]
        start_position_col += dict_directions[direction][1]
        if matrix[start_position_row][start_position_col] != ".":
            print(matrix[start_position_row][start_position_col])

print(*[' '.join(el) for el in matrix],sep='\n')



