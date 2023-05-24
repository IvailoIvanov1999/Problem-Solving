actor_name = input()

points_from_academy = float(input())

number_evaluative = int(input())

points = points_from_academy

for i in range(number_evaluative):
    name_of_evaluative = input()
    points_from_evaluative = float(input())
    points = points +((len(name_of_evaluative)*points_from_evaluative)/2)

    if points > 1250.50:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {points:.1f}!")
        exit(points>1250)
else:
    difference_in_points=abs(1250.50-points)
    print(f"Sorry, {actor_name} you need {difference_in_points:.1f} more!")
