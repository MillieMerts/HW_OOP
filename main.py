class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.finished_courses:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_rate(self):
        if not self.grades:
            return 0
        grades_list = []
        for k in self.grades.values():
            grades_list.extend(k)
        return round(sum(grades_list) / len(grades_list), 1)

    def __str__(self):
        res = \
            f'Имя: {self.name}\n'\
            f'Фамилия: {self.surname}\n'\
            f'Cредняя оценка за домашние задания: {self.average_rate()}\n'\
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n'\
            f'Завершенные курсы: {", ".join(self.finished_courses)}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Студент не найден')
        return self.average_rate() < other.average_rate()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        self.grades = {}


    def average_rate(self):
        if not self.grades:
            return 0
        grades_list = []
        for k in self.grades.values():
            grades_list.extend(k)
        return round(sum(grades_list) / len(grades_list), 1)

    def __str__(self):
        res = \
            f'Имя: {self.name}\n'\
            f'Фамилия: {self.surname}\n'\
            f'Cредняя оценка за лекции: {self.average_rate()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Лектор не найден')
        return self.average_rate() < other.average_rate()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                    student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = \
            f'Имя: {self.name}\n'\
            f'Фамилия: {self.surname}'
        return res


best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']

cool_mentor = Mentor('Some', 'Buddy')
cool_mentor.courses_attached += ['Python']

cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
cool_mentor.rate_hw(best_student, 'Python', 10)
print(best_student.grades)


best_lecturer_1 = Lecturer('Ivan', 'Ivanov')
best_lecturer_1.courses_attached += ['Python', 'Введение в программирование', 'Java']

best_lecturer_2 = Lecturer('Petr', 'Petrov')
best_lecturer_2.courses_attached += ['Java', 'Python']

best_lecturer_3 = Lecturer('Semen', 'Semenov')
best_lecturer_3.courses_attached += ['Java', 'Python', 'Введение в программирование']

cool_reviewer_1 = Reviewer('Michail', 'Michailov')
cool_reviewer_1.courses_attached += ['Python']
cool_reviewer_1.courses_attached += ['Java']

cool_reviewer_2 = Reviewer('Alexander', 'Alexandrov')
cool_reviewer_2.courses_attached += ['Python']
cool_reviewer_2.courses_attached += ['Введение в программирование']

student_1 = Student('Denis', 'Denisov', 'male')
student_1.courses_in_progress += ['Введение в программирование', 'Java']
student_1.finished_courses += ['Python']

student_2 = Student('Maria', 'Maryanova', 'female')
student_2.courses_in_progress += ['Java']
student_2.finished_courses += ['Введение в программирование', 'Python']

student_3 = Student('Ilya', 'Ilyasov', 'male')
student_3.courses_in_progress += ['Python']
student_3.finished_courses += ['Введение в программирование']

student_1.rate_lecturer(best_lecturer_1, 'Python', 10)
student_1.rate_lecturer(best_lecturer_1, 'Введение в программирование', 6)

student_2.rate_lecturer(best_lecturer_2, 'Введение в программирование', 5)
student_2.rate_lecturer(best_lecturer_2, 'Python', 7)
student_2.rate_lecturer(best_lecturer_2, 'Python', 8)

student_3.rate_lecturer(best_lecturer_3, 'Java', 5)
student_3.rate_lecturer(best_lecturer_3, 'Python', 9)
student_3.rate_lecturer(best_lecturer_3, 'Введение в программирование', 7)

cool_reviewer_1.rate_hw(student_1, 'Java', 7)
cool_reviewer_2.rate_hw(student_1, 'Введение в программирование', 9)
cool_reviewer_2.rate_hw(student_2, 'Введение в программирование', 9)
cool_reviewer_2.rate_hw(student_2, 'Python', 9)
cool_reviewer_1.rate_hw(student_3, 'Python', 5)
cool_reviewer_2.rate_hw(student_3, 'Введение в программирование', 6)

student_list = [student_1, student_2, student_3]

def student_rating(student_list, course_name):
    score = 0
    counter = 0
    for student in student_list:
        if course_name in student.grades:
            score += sum(student.grades[course_name])
            counter += len(student.grades[course_name])
    if counter == 0:
        return f'Оценки по курсу {course_name} не найдены'
    else:
        return f'Средняя оценка студента за домашние задания по курсу {course_name} = {round(score / counter, 1)}'

lecturer_list = [best_lecturer_1, best_lecturer_2, best_lecturer_3]

def lecturer_rating(lecturer_list, course_name):
    score = 0
    counter = 0
    for lecturer in lecturer_list:
        if course_name in lecturer.grades:
            score += sum(lecturer.grades[course_name])
            counter += len(lecturer.grades[course_name])
    if counter == 0:
        return f'Оценки по курсу {course_name} не найдены'
    else:
        return f'Средняя оценка лектора за лекции по курсу {course_name} = {round(score / counter, 1)}'

print('=' * 15 + 'Лекторы' + '=' * 15)
print(best_lecturer_1)
print(best_lecturer_2)
print(best_lecturer_3)
print(best_lecturer_1.__lt__(best_lecturer_2))


print('=' * 15 + 'Студенты' + '=' * 15)
print(student_1)
print(student_1.__lt__(student_2))

print('=' * 15 + 'Ревьюверы' + '=' * 15)
print(cool_reviewer_1)

print('=' * 15 + 'Рейтинг по студентам' + '=' * 15)
print(student_rating(student_list, 'Python'))
print(student_rating(student_list, 'Java'))
print(student_rating(student_list, 'Введение в программирование'))

print('=' * 15 + 'Рейтинг по лекторам' + '=' * 15)
print(lecturer_rating(lecturer_list, 'Java'))
print(lecturer_rating(lecturer_list, 'Python'))
print(lecturer_rating(lecturer_list, 'Введение в программирование'))

