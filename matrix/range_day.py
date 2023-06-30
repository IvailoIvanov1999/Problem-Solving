def get_next_position(direction, r, c, steps):
    if direction == "up":
        return (r - steps, c)
    if direction == "down":
        return (r + steps, c)
    if direction == "right":
        return (r, c + steps)
    if direction == "left":
        return (r, c - steps)


def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


matrix = []

char_row, char_col = 0, 0

target_row, target_col = 0, 0
target_count = 0
for rows in range(5):
    elements = input().split()
    matrix.append(elements)
    for columns in range(5):
        el = elements[columns]

        if el == "A":
            char_row, char_col = rows, columns

        elif el == "x":
            target_row, target_col = rows, columns
            target_count += 1

num_commands = int(input())

shooting_direction = {
    "right": lambda r, c: (r, c + 1),
    "left": lambda r, c: (r, c - 1),
    "up": lambda r, c: (r - 1, c),
    "down": lambda r, c: (r + 1, c)
}

hit_target = []

for _ in range(num_commands):
    commands_input = input().split()

    action = commands_input[0]

    direction = commands_input[1]

    if action == "move":
        step = int(commands_input[2])
        next_player_row, next_player_col = get_next_position(direction, char_row, char_col, step)

        if is_outside(next_player_row, next_player_col, 5):
            continue

        if matrix[next_player_row][next_player_col] != ".":
            continue

        matrix[char_row][char_col] = "."
        matrix[next_player_row][next_player_col] = "A"
        char_row, char_col = next_player_row, next_player_col

    else:
        steps = shooting_direction[direction]
        bullet_row, bullet_col = get_next_position(direction,char_row,char_col,1)
        while True:
            if is_outside(bullet_row, bullet_col, 5):
                break
            if matrix[bullet_row][bullet_col] == "x":
                hit_target.append([bullet_row,bullet_col])
                matrix[bullet_row][bullet_col] = "."
                break
            bullet_row,bullet_col=get_next_position(direction,bullet_row,bullet_col,1)
        if target_count == len(hit_target):
            break

if target_count == len(hit_target):
    print(f"Training completed! All {target_count} targets hit.")

else:
    print(f"Training not completed! {target_count - len(hit_target)} targets left.")

for el in hit_target:
    print(el)