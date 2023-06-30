def inside(r, c, s):
    return 0 <= r < s and 0 <= c < s


size = int(input())

matrix = [[x for x in input()] for _ in range(size)]

snake_row, snake_col = 0, 0

for row in range(size):
    for col in range(size):
        if matrix[row][col] == 'S':
            snake_row, snake_col = row, col
            matrix[row][col] = '.'

dict_moves = {
    'left': (0, -1),
    'right': (0, +1),
    'up': (-1, 0),
    'down': (+1, 0)
}

food_quantity = 0
outside = False
while True:

    if food_quantity >= 10:
        print("You won! You fed the snake.")
        break

    move = input()

    snake_row += dict_moves[move][0]
    snake_col += dict_moves[move][1]

    if not (inside(snake_row, snake_col, size)):
        outside = True
        print("Game over!")
        break

    if matrix[snake_row][snake_col] == '*':
        food_quantity += 1

    elif matrix[snake_row][snake_col] == "B":
        matrix[snake_row][snake_col] = '.'
        for row_ in range(snake_row + 1, size):
            for col_ in range(size):
                if matrix[row_][col_] == "B":
                    snake_row, snake_col = row_, col_

    matrix[snake_row][snake_col] = '.'

if not outside:
    matrix[snake_row][snake_col] = 'S'

print(f"Food eaten: {food_quantity}")
print(*[''.join(x) for x in matrix], sep='\n')
