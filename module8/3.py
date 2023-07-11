from peewee import *

conn = SqliteDatabase('db2.sqlite')


class Students(Model):
    id = PrimaryKeyField(column_name='id', unique=True)
    name = CharField(column_name='name')
    surname = CharField(column_name='surname')
    age = IntegerField(column_name='age')
    city = CharField(column_name='city')

    class Meta:
        database = conn


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

# s = Students.create(id=1, name='Max', surname='Brooks', age=24, city='Spb')
# s = Students.create(id=2, name='John', surname='Stones', age=15, city='Spb')
# s = Students.create(id=3, name='Andy', surname='Wings', age=45, city='Manchester')
# s = Students.create(id=4, name='Kate', surname='Brooks', age=34, city='Spb')
#
# c = Courses.create(id=1, name='python', time_start='21.07.21', time_end='21.08.21')
# c = Courses.create(id=2, name='java', time_start='13.07.21', time_end='16.08.21')
#
# s_c = StudentCourse.create(student_id=1, course_id=1)
# s_c = StudentCourse.create(student_id=2, course_id=1)
# s_c = StudentCourse.create(student_id=3, course_id=1)
# s_c = StudentCourse.create(student_id=4, course_id=2)

query_age = (Students
             .select()
             .where(Students.age > 30))
print('Студенты старше 30 лет:')
for student in query_age:
    print(student.name, student.surname)

query_course = (Students
                .select()
                .join(StudentCourse)
                .where(StudentCourse.course_id == 1))
print('____________________________________')
print('Студенты изучающие python:')
for student in query_course:
    print(student.name, student.surname)

query_course_city = (Students
                     .select()
                     .join(StudentCourse)
                     .where(StudentCourse.course_id == 1, Students.city == 'Spb'))
print('____________________________________')
print('Студенты изучающие python и проживающие в Санкт-Петербурге:')
for student in query_course_city:
    print(student.name, student.surname)
