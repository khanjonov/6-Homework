import sqlite3

conn = sqlite3.connect("university.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    student_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER CHECK(age > 0),
    email TEXT UNIQUE NOT NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    course_code TEXT UNIQUE NOT NULL,
    credits INTEGER CHECK(credits BETWEEN 1 AND 5)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS enrollments (
    enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE SET NULL
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    experience_years INTEGER CHECK(experience_years >= 0)
);
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS course_assignments (
    assignment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    teacher_id INTEGER,
    course_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON DELETE SET DEFAULT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id) ON DELETE CASCADE
);
""")

students_data = [
    ("Bobur", 20, "bobur@example.com"),
    ("Boltaboy", 22, "boltaboy@example.com"),
    ("Kolya", 21, "kolya@example.com"),
    ("Diana", 19, "diana@example.com"),
    ("Emilia", 23, "emilia@example.com"),
    ("Frank", 20, "frank@example.com"),
    ("Ali", 22, "ali@example.com")
]
cursor.executemany("INSERT INTO students (name, age, email) VALUES (?, ?, ?);", students_data)

courses_data = [
    ("Mathematics", "MATH101", 3),
    ("History", "HIST201", 2),
    ("Computer Science", "CS301", 4)
]
cursor.executemany("INSERT INTO courses (course_name, course_code, credits) VALUES (?, ?, ?);", courses_data)

teachers_data = [
    ("Prof. Smith", 10),
    ("Dr. Johnson", 5)
]
cursor.executemany("INSERT INTO teachers (name, experience_years) VALUES (?, ?);", teachers_data)

course_assignments_data = [
    (1, 1),
    (2, 2)
]
cursor.executemany("INSERT INTO course_assignments (teacher_id, course_id) VALUES (?, ?);", course_assignments_data)

cursor.execute("ALTER TABLE students RENAME TO learners;")

cursor.execute("ALTER TABLE learners RENAME COLUMN age TO student_age;")

cursor.execute("UPDATE learners SET student_age = 25 WHERE name = 'Alice';")
cursor.execute("UPDATE learners SET student_age = 24 WHERE name = 'Bob';")

cursor.execute("DELETE FROM learners WHERE name = 'Charlie';")
cursor.execute("DELETE FROM learners WHERE name = 'Diana';")

conn.commit()
conn.close()

