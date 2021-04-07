class Student:

    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached and 1 <= grade <= 10:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            print('Ошибка')
            return 'Ошибка'
            

        

class Mentor:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        

class Lecturer(Mentor):
    
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

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




 
new_lecturer = Lecturer('Vasiliy', 'Petrov')
new_reviewer = Reviewer('Andrey', 'Grachev')
new_student = Student('Gennadiy', 'Sidorov', 'м')
print(new_lecturer.name)
print(new_reviewer.surname)
print(new_student.name, new_student.surname)
print('')

print(new_reviewer.courses_attached)
new_reviewer.courses_attached += ['Python', 'Git']
new_lecturer.courses_attached += ['Python', 'Git']
new_student.courses_in_progress += ['Python', 'Git']
print(new_reviewer.courses_attached)
print(new_student.courses_in_progress)
print('')

new_reviewer.rate_hw(new_student, 'Python', 20)
print(new_student.grades)
print('')

new_student.rate_lecture(new_lecturer, 'Git', 10)
print(new_lecturer.grades)
print('')
