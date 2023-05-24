students_dictionary = {}
while True:
    data_input = input()
    if ":" not in data_input:
        break

    students_name, students_id, students_course = data_input.split(":")
    students_course = students_course.lower()

    if students_course not in students_dictionary:
        students_dictionary[students_course] = {students_id: students_name}

    else:
        students_dictionary[students_course][students_id] = students_name

course_name = " ".join(data_input.split("_"))
students = students_dictionary[course_name]

for id, name in students.items():
    print(f"{name} - {id}")
