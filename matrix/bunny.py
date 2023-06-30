def is_inside(r, c, size):
    return 0 <= r < size and 0 <= c < size


n = int(input())

matrix = []

bunny_row, bunny_col = 0, 0
best_direction = ""
best_path = []
for row in range(n):
    elements = input().split()
    matrix.append(elements)
    for col in range(n):
        element = elements[col]
        if element == "B":
            bunny_row, bunny_col = row, col

directions = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}
max_eggs = float("-inf")
for dir, steps in directions.items():
    eggs = 0
    current_row, current_col = bunny_row, bunny_col
    path = []
    while True:
        current_row, current_col = steps(current_row, current_col)
        if not is_inside(current_row, current_col, n):
            break

        if matrix[current_row][current_col] == "X":
            break
        eggs += int(matrix[current_row][current_col])
        path.append([current_row, current_col])
    if eggs > max_eggs:
        max_eggs, best_direction, best_path = eggs, dir, path


print(best_direction)
for step in best_path:
    print(step)
print(max_eggs)


# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0