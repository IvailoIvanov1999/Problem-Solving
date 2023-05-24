def is_not_valid_index(row,col,rows,cols):
    return row < 0 or col < 0 or row >= rows or col >= cols

rows, columns = [int(x) for x in input().split()]

matrix = [[x for x in input().split()] for _ in range(rows)]

negative = False

while True:
    command = input().split()

    if command[0] == "END":
        break

    if (int(command[1]) or int(command[2]) or int(command[3]) or int(command[4])) < 0:
        negative = True

    if negative or command[0]!="swap" or len(command) != 5:
            # int(command[1]) or int(command[2]) or int(command[3]) or int(command[4])) not in range(len(matrix)):
        print("Invalid input!")
        continue






    row_1, col_1, row_2, col_2 = int(command[1]), int(command[2]), int(command[3]), int(command[4])

    if is_not_valid_index(row_1,col_1,rows,columns) or is_not_valid_index(row_2,col_2,rows,columns):
        print("Invalid input!")
        continue

    f_value = matrix[row_1][col_1]
    s_value = matrix[row_2][col_2]

    matrix[row_1][col_1] = s_value
    matrix[row_2][col_2] = f_value

    [print(*x) for x in matrix]

# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
