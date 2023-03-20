n = int(input())
students_dict = {}
flag = False
for _ in range(n):

    student_name = input()
    grade = float(input())

    if student_name not in students_dict:
        students_dict[student_name] = [grade]


    else:
        students_dict[student_name] += [grade]

        summing_grades = sum(students_dict[student_name])

        average_grade = summing_grades / len(students_dict[student_name])

        students_dict[student_name] = [average_grade]

for k, v in students_dict.items():
    v = float(*v)
    if v >= 4.50:
         print(f"{k} -> {v:.2f}")


