from math import floor
number_of_tournaments_played = int(input())

starting_points_in_ranklist = int(input())

points_after_tournament = starting_points_in_ranklist

winn = 2000
final = 1200
semi_final = 720

win_times = 0
average_points_from_tournament = 0
for i in range(number_of_tournaments_played):
    stage_from_tournament = input()

    if stage_from_tournament == "W":
        points_after_tournament += winn

        win_times = win_times + 1
        average_points_from_tournament = average_points_from_tournament + winn

    elif stage_from_tournament == "F":
        average_points_from_tournament = average_points_from_tournament + final
        points_after_tournament += final

    elif stage_from_tournament == "SF":
        average_points_from_tournament = average_points_from_tournament + semi_final
        points_after_tournament += semi_final

points_average = average_points_from_tournament / number_of_tournaments_played

percent_won_toournaments = (win_times / number_of_tournaments_played) * 100

print(f"Final points: {points_after_tournament}")
print(f"Average points: {floor(int(points_average))}")
print(f"{percent_won_toournaments:.2f}%")