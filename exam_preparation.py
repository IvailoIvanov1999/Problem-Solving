bad_grades_count = int(input())

failed_times = 0
counter_exercises = 0
average_grade = 0
last_exercise = ""
solved_exercises = 0
has_failed = True

while failed_times < bad_grades_count:
    exercise_name = input()
    grade = int(input())

    if exercise_name == "Enough":
        has_failed = False
        break

    if grade <= 4:
        failed_times += 1

    average_grade += grade
    last_exercise = exercise_name
    solved_exercises += 1

    if has_failed:

        print(f"Average score: {(average_grade / solved_exercises):.2f}")

        print(f"Number of problems: {solved_exercises}")

        print(f"Last problem: {last_exercise}")
        break


    elif failed_times >= bad_grades_count:

        print(f"You need a break, {bad_grades_count} poor grades.")


