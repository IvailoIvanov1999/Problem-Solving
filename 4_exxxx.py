students_on_exam = int(input())
grades_calculator = 0
group_1 = 0
group_2 = 0
group_3 = 0
group_4 = 0

for i in range(students_on_exam):
    grade_of_exam = float(input())

    grades_calculator = grades_calculator + grade_of_exam

    if grade_of_exam >= 5.00:
        group_1 += 1

    elif 4 <= grade_of_exam <= 4.99:
        group_2 += 1

    elif 3 <= grade_of_exam <= 3.99:
        group_3 += 1

    elif grade_of_exam < 3:
        group_4 += 1




average = grades_calculator / students_on_exam
failed = group_4 / students_on_exam * 100
between_3 = group_3 / students_on_exam * 100
between_2 = group_2 / students_on_exam * 100
top = group_1 / students_on_exam * 100


print(f"Top students: {top:.2f}%")
print(f"Between 4.00 and 4.99: {between_2:.2f}%")
print(f"Between 3.00 and 3.99: {between_3:.2f}%")
print(f"Fail: {failed:.2f}%")
print(f"Average: {average:.2f}")
