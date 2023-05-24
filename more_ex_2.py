from math import floor


def center_point_coordinates(num1, num2, num3, num4):
    return (num3 - num1) ** 2 + (num4 - num2) ** 2


number_1_x1 = float(input())
number_2_y1 = float(input())
number_3_x2 = float(input())
number_4_y2 = float(input())

distance_x1_y1 = center_point_coordinates(number_1_x1, number_2_y1, 0, 0)
distance_x2_y2 = center_point_coordinates(number_3_x2, number_4_y2, 0, 0)

if distance_x1_y1 > distance_x2_y2:
    print(f'({int(floor(number_3_x2))}, {int(floor(number_4_y2))})')
elif distance_x1_y1 <= distance_x2_y2:
    print(f'({int(floor(number_1_x1))}, {int(floor(number_2_y1))})')


