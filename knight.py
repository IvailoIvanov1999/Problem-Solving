def is_inside(board, row, col):
    board_size = len(board)
    if row < 0 or col < 0 or row >= board_size or col >= board_size:
        return False
    return board[row][col] == "K"


def count_affected_knights(board, row, col):
    result = 0
    if is_inside(board, row - 2, col - 1):
        result += 1
    if is_inside(board, row - 2, col + 1):
        result += 1
    if is_inside(board, row + 2, col + 1):
        result += 1
    if is_inside(board, row + 2, col - 1):
        result += 1
    if is_inside(board, row - 1, col - 2):
        result += 1
    if is_inside(board, row - 1, col + 2):
        result += 1
    if is_inside(board, row + 1, col - 2):
        result += 1
    if is_inside(board, row + 1, col + 2):
        result += 1
    return result


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(list(input()))

removed_knights = 0

while True:
    max_count, knight_row, knight_col = 0, 0, 0

    for r in range(n):
        for c in range(n):
            if matrix[r][c] == "0":
                continue

            count = count_affected_knights(matrix, r, c)

            if count > max_count:
                max_count, knight_row, knight_col = count, r, c

    if max_count == 0:
        break
    matrix[knight_row][knight_col] = "0"
    removed_knights += 1

print(removed_knights)

# 5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
