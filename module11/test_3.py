from peewee import *
import unittest

conn = SqliteDatabase('db4.sqlite')


class Students(Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn

    @staticmethod
    def add_student(id, name, surname, age, city, course_id):
        if Students.get_or_none(Students.id == id) is not None:
            print('Студент с таким id уже существует!!!')
        elif Courses.get_or_none(Courses.id == course_id) is None:
            print('Такого курса нет!!!')
        else:
            Students.create(id=id, name=name, surname=surname, age=age, city=city)
            StudentCourse.create(student_id=id, course_id=course_id)

    @staticmethod
    def del_student(name, surname):
        remove_student = (Students.get_or_none(Students.name == name, Students.surname == surname))
        course_remove_student = StudentCourse.get_or_none(StudentCourse.student_id == remove_student.id)
        if remove_student is None:
            print('Такого студента нет!!!')
        else:
            remove_student.delete_instance()
            course_remove_student.delete_instance()


class Courses(Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name='name')
    time_start = CharField(column_name='time_start')
    time_end = CharField(column_name='time_end')

    class Meta:
        database = conn


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
# #
# StudentCourse.create(student_id=1, course_id=1)
# StudentCourse.create(student_id=2, course_id=1)
# StudentCourse.create(student_id=3, course_id=1)
# StudentCourse.create(student_id=4, course_id=2)


# Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
# Students.del_student('Олег', 'Петров')


query_course = (Students
                .select()
                .join(StudentCourse)
                .where(StudentCourse.course_id == 1))
print('____________________________________')
print('Студенты изучающие python:')
for student in query_course:
    print(student.name, student.surname)

print('____________________________________')
print('Все студенты:')
for student in Students.select():
    print(student.name, student.surname)


class TestAddStudent(unittest.TestCase):

    def test1(self):
        # Сравнение длинны списков студентов до и после добавления
        students_before = []
        students_after = []
        # Список студентов до добавления студента
        for student in Students.select():
            students_before.append(student.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        # Список студентов после добавления студента
        for student in Students.select():
            students_after.append(student.id)
        Students.del_student('Олег', 'Петров')
        self.assertNotEqual(len(students_before), len(students_after))

    def test2(self):
        # Сравнение длинны списков курсов студентов до и после добавления
        student_course_before = []
        student_course_after = []
        # Список курсов студентов до добавления студента
        for stud_course in StudentCourse.select():
            student_course_before.append(stud_course.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        # Список курсов студентов после добавления студента
        for stud_course in StudentCourse.select():
            student_course_after.append(stud_course.id)
        Students.del_student('Олег', 'Петров')
        self.assertNotEqual(len(student_course_before), len(student_course_after))

    def test3(self):
        # Проверка того, что добавился только один студент
        students_before = []
        students_after = []
        for student in Students.select():
            students_before.append(student.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for student in Students.select():
            students_after.append(student.id)
        Students.del_student('Олег', 'Петров')
        self.assertEqual((len(students_after) - len(students_before)), 1)

    def test4(self):
        # Проверка того, что добавилась только одна запись в таблицу StudentCourse
        student_course_before = []
        student_course_after = []
        for stud_course in StudentCourse.select():
            student_course_before.append(stud_course.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for stud_course in StudentCourse.select():
            student_course_after.append(stud_course.id)
        Students.del_student('Олег', 'Петров')
        self.assertEqual((len(student_course_after) - len(student_course_before)), 1)

    def test5(self):
        # Проверка того, что добавился именно тот студент, который был указан в функции
        students_before = set()
        students_after = set()
        for student in Students.select():
            students_before.add((student.name, student.surname))
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for student in Students.select():
            students_after.add((student.name, student.surname))
        Students.del_student('Олег', 'Петров')
        new_student = (list(students_before.symmetric_difference(students_after)))
        self.assertTrue(new_student == [('Олег', 'Петров')])

    def test6(self):
        # Проверка того, что добавилась необходимая запись в таблицу StudentCourse
        student_course_before = set()
        student_course_after = set()
        for stud_course in StudentCourse.select():
            student_course_before.add(stud_course.id)
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for stud_course in StudentCourse.select():
            student_course_after.add(stud_course.id)
        Students.del_student('Олег', 'Петров')
        new_course_student = (list(student_course_before.symmetric_difference(student_course_after)))
        self.assertTrue(new_course_student == [5])


class TestDelStudent(unittest.TestCase):

    def test1(self):
        # Сравнение длинны списков студентов до и после удаления
        students_before = []
        students_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        # Список студентов до удаления студента
        for student in Students.select():
            students_before.append(student.id)
        Students.del_student('Олег', 'Петров')
        # Список студентов после удаления студента
        for student in Students.select():
            students_after.append(student.id)
        self.assertNotEqual(len(students_before), len(students_after))

    def test2(self):
        # Сравнение длинны списков курсов студентов до и после удаления
        student_course_before = []
        student_course_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        # Список курсов студентов до удаления студента
        for stud_course in StudentCourse.select():
            student_course_before.append(stud_course.id)
        Students.del_student('Олег', 'Петров')
        # Список курсов студентов после удаления студента
        for stud_course in StudentCourse.select():
            student_course_after.append(stud_course.id)
        self.assertNotEqual(len(student_course_before), len(student_course_after))

    def test3(self):
        # Проверка того, что удалили только одного студента
        students_before = []
        students_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for student in Students.select():
            students_before.append(student.id)
        Students.del_student('Олег', 'Петров')
        for student in Students.select():
            students_after.append(student.id)
        self.assertEqual((len(students_before) - len(students_after)), 1)

    def test4(self):
        # Проверка того, что удалилась только одна запись в таблице StudentCourse
        student_course_before = []
        student_course_after = []
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for stud_course in StudentCourse.select():
            student_course_before.append(stud_course.id)
        Students.del_student('Олег', 'Петров')
        for stud_course in StudentCourse.select():
            student_course_after.append(stud_course.id)
        self.assertEqual((len(student_course_before) - len(student_course_after)), 1)

    def test5(self):
        # Проверка того, что удалился именно тот студент, который был указан в функции
        students_before = set()
        students_after = set()
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for student in Students.select():
            students_before.add((student.name, student.surname))
        Students.del_student('Олег', 'Петров')
        for student in Students.select():
            students_after.add((student.name, student.surname))
        remove_student = (list(students_before.symmetric_difference(students_after)))
        self.assertTrue(remove_student == [('Олег', 'Петров')])

    def test6(self):
        # Проверка того, что удалилась необходимая запись в таблице StudentCourse
        student_course_before = set()
        student_course_after = set()
        Students.add_student(5, 'Олег', 'Петров', 32, 'Pskov', 1)
        for stud_course in StudentCourse.select():
            student_course_before.add(stud_course.id)
        Students.del_student('Олег', 'Петров')
        for stud_course in StudentCourse.select():
            student_course_after.add(stud_course.id)
        delete_entry = (list(student_course_before.symmetric_difference(student_course_after)))
        self.assertTrue(delete_entry == [5])
