from peewee import *
import unittest

conn = SqliteDatabase('db3.sqlite')


class Students(Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn

    @staticmethod
    def add_student(id, name, surname, age, city):
        Students.create(id=id, name=name, surname=surname, age=age, city=city)

    @staticmethod
    def del_student(name, surname):
        remove_student = (Students.get_or_none(Students.name == name, Students.surname == surname))
        if remove_student is None:
            print('Такого студента нет!!!')
        else:
            remove_student.delete_instance()


class Courses(Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')

    class Meta:
        database = conn

    @staticmethod
    def add_course(id, name, time_start, time_end):
        Courses.create(id=id, name=name, time_start=time_start, time_end=time_end)

    @staticmethod
    def del_course(name):
        remove_course = (Courses.get_or_none(Courses.name == name))
        if remove_course is None:
            print('Такого курса нет!!!')
        else:
            remove_course.delete_instance()


class StudentCourse(Model):
    student_id = ForeignKeyField(Students)
    course_id = ForeignKeyField(Courses)

    class Meta:
        database = conn


# Students.create_table()
# Courses.create_table()
# StudentCourse.create_table()
#
# Students.create(id=1, name='Max', surname='Brooks', age=24, city='Spb')
# Students.create(id=2, name='John', surname='Stones', age=15, city='Spb')
# Students.create(id=3, name='Andy', surname='Wings', age=45, city='Manchester')
# Students.create(id=4, name='Kate', surname='Brooks', age=34, city='Spb')
#
# Courses.create(id=1, name='python', time_start='21.07.21', time_end='21.08.21')
# Courses.create(id=2, name='java', time_start='13.07.21', time_end='16.08.21')
#
# StudentCourse.create(student_id=1, course_id=1)
# StudentCourse.create(student_id=2, course_id=1)
# StudentCourse.create(student_id=3, course_id=1)
# StudentCourse.create(student_id=4, course_id=2)


# Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
# Courses.add_course(3, 'SQL', time_start='25.01.24', time_end='02.03.24')
# Students.del_student('Олег', 'Петров')
# Courses.del_course('SQL')

print('____________________________________')
print('Все студенты:')
for student in Students.select():
    print(student.name, student.surname)

print('____________________________________')
print('Все курсы:')
for course in Courses.select():
    print(course.name)


class TestAddStudent(unittest.TestCase):

    def test1(self):
        # Сравнение длинны списков студентов до и после добавления
        students_before = []
        students_after = []
        # Список студентов до добавления студента
        for student in Students.select():
            students_before.append(student.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        # Список студентов после добавления студента
        for student in Students.select():
            students_after.append(student.id)
        Students.del_student('Олег', 'Петров')
        self.assertNotEqual(len(students_before), len(students_after))

    def test2(self):
        # Проверка того, что добавился только один студент
        students_before = []
        students_after = []
        for student in Students.select():
            students_before.append(student.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        for student in Students.select():
            students_after.append(student.id)
        Students.del_student('Олег', 'Петров')
        self.assertEqual((len(students_after) - len(students_before)), 1)

    def test3(self):
        # Проверка того, что добавился именно тот студент, который был указан в функции
        students_before = set()
        students_after = set()
        for student in Students.select():
            students_before.add((student.name, student.surname))
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        for student in Students.select():
            students_after.add((student.name, student.surname))
        Students.del_student('Олег', 'Петров')
        new_student = (list(students_before.symmetric_difference(students_after)))
        self.assertTrue(new_student == [('Олег', 'Петров')])


class TestAddCourse(unittest.TestCase):

    def test1(self):
        # Сравнение длинны списков курсов до и после добавления
        courses_before = []
        courses_after = []
        # Список курсов до добавления курса
        for course in Courses.select():
            courses_before.append(course.name)
        Courses.add_course(3, 'SQL', time_start='25.01.24', time_end='02.03.24')
        # Список курсов после добавления студента
        for course in Courses.select():
            courses_after.append(course.name)
        Courses.del_course('SQL')
        self.assertNotEqual(len(courses_before), len(courses_after))

    def test2(self):
        # Проверка того, что добавился только один курс
        courses_before = []
        courses_after = []
        for course in Courses.select():
            courses_before.append(course.name)
        Courses.add_course(3, 'SQL', time_start='25.01.24', time_end='02.03.24')
        for course in Courses.select():
            courses_after.append(course.name)
        Courses.del_course('SQL')
        self.assertEqual((len(courses_after) - len(courses_before)), 1)

    def test3(self):
        # Проверка того, что добавился именно тот курс, который был указан в функции
        courses_before = set()
        courses_after = set()
        for course in Courses.select():
            courses_before.add(course.name)
        Courses.add_course(3, 'SQL', time_start='25.01.24', time_end='02.03.24')
        for course in Courses.select():
            courses_after.add(course.name)
        Courses.del_course('SQL')
        new_course = (list(courses_before.symmetric_difference(courses_after)))
        self.assertTrue(new_course == ['SQL'])

class TestDelStudent(unittest.TestCase):

    def test1(self):
        # Сравнение длинны списков студентов до и после удаления
        students_before = []
        students_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        # Список студентов до удаления студента
        for student in Students.select():
            students_before.append(student.id)
        Students.del_student('Олег', 'Петров')
        # Список студентов после удаления студента
        for student in Students.select():
            students_after.append(student.id)
        self.assertNotEqual(len(students_before), len(students_after))

    def test2(self):
        # Проверка того, что удалили только одного студента
        students_before = []
        students_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        for student in Students.select():
            students_before.append(student.id)
        Students.del_student('Олег', 'Петров')
        for student in Students.select():
            students_after.append(student.id)
        self.assertEqual((len(students_before) - len(students_after)), 1)

    def test3(self):
        # Проверка того, что удалился именно тот студент, который был указан в функции
        students_before = set()
        students_after = set()
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov')
        for student in Students.select():
            students_before.add((student.name, student.surname))
        Students.del_student('Олег', 'Петров')
        for student in Students.select():
            students_after.add((student.name, student.surname))
        remove_student = (list(students_before.symmetric_difference(students_after)))
        self.assertTrue(remove_student == [('Олег', 'Петров')])

