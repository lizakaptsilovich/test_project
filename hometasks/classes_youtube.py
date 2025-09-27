class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_students(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

s1 = Student('Tim', 12, 10)
s2 = Student('Jim', 22, 8)

course = Course('science', 1)
course.add_students(s1)
print(course.students[0].name)