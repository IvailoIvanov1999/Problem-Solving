data = input()
courses = {}
while data != "end":
    course_name, student_name = data.split(" : ")

    key = course_name
    value = student_name

    if key not in courses:
        courses[key] = [value]
    else:
        courses[key] += [value]
    data = input()

for k, v in courses.items():
    print(f"{k}: {len(v)}")
    for item in v:
        print(f"-- {item}")
