matrix = [[x for x in input().split()] for _ in range(6)]

# bucket_row, bucket_col = 0, 0


scored_points = 0

for _ in range(3):

    throw_cords_input = input().strip('(').strip(')').split(', ')
    throw_row = int(throw_cords_input[0])
    throw_col = int(throw_cords_input[1])
    if not (0 <= throw_row < 6 and 0 <= throw_col < 6):
        continue

    elif matrix[throw_row][throw_col] == 'B':
        for el in range(6):
            elem = matrix[el][throw_col]
            if elem.isalpha():
                continue
            scored_points += int(elem)

        matrix[throw_row][throw_col] = '.'

    else:
        continue


if scored_points < 100:
    print(f"Sorry! You need {100 - scored_points} points more to win a prize.")

elif 100 <= scored_points <= 199:
    print(f"Good job! You scored {scored_points} points, and you've won Football.")

elif 200 <= scored_points <= 299:
    print(f"Good job! You scored {scored_points} points, and you've won Teddy Bear.")

elif 300 <= scored_points:
    print(f"Good job! You scored {scored_points} points, and you've won Lego Construction Set.")
