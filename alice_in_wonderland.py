def is_outside(row, col, size):
    if row < 0 or col < 0 or row >= size or col >= size:
        return True
    return False


def get_next_position(direction, r, c):
    if direction == "up":
        return (r - 1, c)
    if direction == "down":
        return (r + 1, c)
    if direction == "right":
        return (r, c + 1)
    if direction == "left":
        return (r, c - 1)


size = int(input())

matrix = []

alice_location_row, alice_location_col = 0, 0

for row in range(size):
    element = input().split()
    matrix.append(element)
    for col in range(size):
        el = element[col]

        if el == "A":
            alice_location_row, alice_location_col = row, col

matrix[alice_location_row][alice_location_col] = "*"
alice_tea_bags = 0

while True:
    commands = input()
    alice_location_row, alice_location_col = get_next_position(commands, alice_location_row, alice_location_col)
    if is_outside(alice_location_row, alice_location_col, size):
        break
    cell = matrix[alice_location_row][alice_location_col]
    matrix[alice_location_row][alice_location_col] = "*"

    if cell == "R":
        break

    if cell.isdigit():
        number = int(cell)
        alice_tea_bags += number
        if alice_tea_bags >= 10:
            break

if alice_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for el in matrix:
    print(" ".join(el))
