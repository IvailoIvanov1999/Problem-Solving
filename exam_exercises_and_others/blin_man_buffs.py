n, m = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(n)]

my_curr_row = 0
my_curr_col = 0
players = 3
players_catch = 0
moves_count = 0

return_row_cords = 0
return_col_cords = 0
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
    my_curr_row = rows
    my_curr_col = cols

    if c == "up":
        my_curr_row += navigations[0][0]
        my_curr_col += navigations[0][1]


    if c == "down":
        my_curr_row += navigations[1][0]
        my_curr_col += navigations[1][1]


    if c == "left":
        my_curr_row += navigations[2][0]
        my_curr_col += navigations[2][1]


    if c == "right":
        my_curr_row += navigations[3][0]
        my_curr_col += navigations[3][1]


    return my_curr_row, my_curr_col


for row in range(n):
    for col in range(m):
        if matrix[row][col] == "B":
            my_curr_row, my_curr_col = row, col
            matrix[my_curr_row][my_curr_col] = '-'

while True:
    command = input()
    if command == "Finish" or players <= 0:
        break

    return_row_cords,return_col_cords = my_curr_row,my_curr_col

    my_curr_row, my_curr_col = moves(command, my_curr_row, my_curr_col)

    if 0 <= my_curr_row < n and 0 <= my_curr_col < m:

        if matrix[my_curr_row][my_curr_col] == "P":
            players -= 1
            players_catch += 1
            matrix[my_curr_row][my_curr_col] = '-'
            moves_count += 1


        elif matrix[my_curr_row][my_curr_col] == "-":
            moves_count += 1


        elif matrix[my_curr_row][my_curr_col] == "O":
            my_curr_row,my_curr_col = return_row_cords,return_col_cords

            continue
    else:
        my_curr_row, my_curr_col = return_row_cords, return_col_cords
        continue

print("Game over!")
print(f"Touched opponents: {players_catch} Moves made: {moves_count}")
