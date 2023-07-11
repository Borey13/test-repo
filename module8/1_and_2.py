import sqlite3

conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()


def my_print(data):
    for i in data:
        print(i[0], i[1])


# cursor.execute('''CREATE TABLE Students
#                 (id int PRIMARY KEY,
#                 name Varchar(32),
#                 surname Varchar(32),
#                 age int,
#                 city Varchar(32))''')
#
# cursor.execute('''CREATE TABLE Courses
#                 (id int PRIMARY KEY,
#                 name Varchar(32),
#                 time_start text,
#                 time_end text)''')
#
#
# cursor.execute('''CREATE TABLE Student_course
#                 (student_id int,
#                 course_id int,
#                 FOREIGN KEY (student_id) REFERENCES Students(id),
#                 FOREIGN KEY (course_id) REFERENCES Courses(id))''')
# #
# cursor.executemany('INSERT INTO Students VALUES (?,?,?,?,?)',
#                    [(1, 'Max', 'Brooks', 24, 'Spb'),
#                     (2, 'John', 'Stones', 15, 'Spb'),
#                     (3, 'Andy', 'Wings', 45, 'Manchester'),
#                     (4, 'Kate', 'Brooks', 34, 'Spb')])
#
# cursor.executemany('INSERT INTO Courses VALUES (?,?,?,?)',
#                    [(1, 'python', '21.07.21', '21.08.21'),
#                     (2, 'java', '13.07.21', '16.08.21')])
#
# cursor.executemany('INSERT INTO Student_course VALUES (?,?)',
#                    [(1, 1),
#                     (2, 1),
#                     (3, 1),
#                     (4, 2)])
#
# conn.commit()

cursor.execute('SELECT name, surname FROM Students WHERE age > 30')
print('Студенты старше 30 лет:')
my_print(cursor.fetchall())

cursor.execute('''SELECT Students.name, Students.surname
                FROM Students 
                INNER JOIN Student_course ON Students.id = student_id
                INNER JOIN Courses ON Courses.id == course_id
                WHERE Courses.name == "python"''')
print('____________________________________')
print('Студенты изучающие python:')
my_print(cursor.fetchall())

cursor.execute('''SELECT Students.name, Students.surname 
                FROM Students 
                INNER JOIN Student_course ON Students.id = student_id
                INNER JOIN Courses ON Courses.id == course_id
                WHERE Courses.name == "python" and Students.city == "Spb"''')
print('____________________________________')
print('Студенты изучающие python, проживающие в Санкт-Петербурге:')
my_print(cursor.fetchall())
