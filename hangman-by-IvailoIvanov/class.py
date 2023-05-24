class Class:
    __students_count = 22

    def __init__(self, name):
        self.name_class = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        if len(self.students) < self.__students_count:
            self.students.append(name)
            self.grades.append(grade)

    def get_average_grade(self):
        if len(self.grades)==0:
            return 0
        average = sum(self.grades) / len(self.grades)
        return float(f'{average:.2f}')

    def __repr__(self):

        result=(f"The students in {self.name_class}: {', '.join(self.students)}. Average grade: {self.get_average_grade()}")
        return (result)

a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)
print(a_class)
