class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {} 

    def __str__(self):
        return (f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за домашние задания: {self.average_grade()}
Изучаемые курсы: {self.courses_in_progress}
Пройденные курсы: {self.finished_courses}""")


    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')
            return 'Ошибка'

    def average_grade(self):
        sum_ = 0
        cnt = 0
        for course in self.grades.values():
            for grade in course:
                sum_ += grade
                cnt += 1
        return sum_ / cnt


class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_grade(self):
        sum_ = 0
        cnt = 0
        for course in self.grades.values():
            for grade in course:
                sum_ += grade
                cnt += 1
        return sum_ / cnt
    
    def __str__(self):
        return (f"""Имя: {self.name}
Фамилия: {self.surname}
Средняя оценка за лекции: {self.average_grade()}""")


class Reviewer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress and 1 <= grade <= 10:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            print('Ошибка')
            return 'Ошибка'
    
    def __str__(self):
        return (f"""Имя: {self.name}
Фамилия: {self.surname}""")




 
new_lecturer = Lecturer('Vasiliy', 'Petrov')
new_reviewer = Reviewer('Andrey', 'Grachev')
new_student = Student('Gennadiy', 'Sidorov', 'м')
print(new_lecturer.name)
print(new_reviewer.surname)
print(new_student.name, new_student.surname)
print()


print(new_reviewer.courses_attached)
new_reviewer.courses_attached += ['Python', 'Git']
new_lecturer.courses_attached += ['Python', 'Git']
new_student.courses_in_progress += ['Python', 'Git']
print(new_reviewer.courses_attached)
print(new_student.courses_in_progress)
print()


new_reviewer.rate_hw(new_student, 'Python', 20)
new_reviewer.rate_hw(new_student, 'Python', 8)
new_reviewer.rate_hw(new_student, 'Python', 10)
new_reviewer.rate_hw(new_student, 'Git', 6)
print(new_student.grades)
print()

new_student.rate_lecture(new_lecturer, 'Git', 8)
new_student.rate_lecture(new_lecturer, 'Python', 10)
print(new_lecturer.grades)
print()


print(new_student.average_grade())
print(new_lecturer.average_grade())
print()


print(new_student)
print()
print(new_reviewer)
print()
print(new_lecturer)
print()

