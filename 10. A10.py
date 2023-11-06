import sqlite3

conn = sqlite3.connect('IIIT_Kalyani.db')
cur = conn.cursor()

# def execute_query(query):
#     connection = sqlite3.connect("IIIT_Kalyani.db")
#     cursor = connection.cursor()
#     cursor.execute(query)
#     result = cursor.fetchall()
#     connection.close()
#     return result

print("Opened database successfully")

cur.execute("DROP TABLE IF EXISTS Students")
cur.execute("DROP TABLE IF EXISTS Courses")
cur.execute("DROP TABLE IF EXISTS Enrollment")

cur.execute(''' CREATE TABLE IF NOT EXISTS Students
        (rollno INT PRIMARY KEY,
        name TEXT,
        phoneno INT,
        grade CHAR(2));''')

print("Table- Students created successfully")


cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(101,'Ajay',9199,'EX'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(102,'Aman',8719,'B'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(103,'Ayushi',7824,'B'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(104,'Chirag',8731,'C'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(105,'Akash',7865,'D'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(110,'Kunal',9314,'A'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(106,'Saurabh',7317,'F'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(107,'Prakhar',9521,'P'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(108,'Himanshu',3416,'P'))

cur.execute("INSERT INTO Students (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(109,'Bhavesh',8965,'EX'))


#DUSRI TABLE BNA RHE - COURSE
cur.execute('''
    CREATE TABLE IF NOT EXISTS Courses (
        course_id INTEGER PRIMARY KEY,
        course_name TEXT,
        instructor TEXT
    )
''')

print("Table- Courses created successfully")

courses_data = [
    (1, 'Computer Science (101)', 'Dr. Blue'),
    (2, 'Mathematics (201)', 'Prof. Hero'),
    (3, 'Physics (301)', 'Dr. Brown'),
    (4, 'bio (401)', 'Dr. Shagun'),
    (5, 'Metallurgy (501)', 'Dr. Ananya'),
    (6, 'Mining (301)', 'Dr. Charles'),
]

cur.executemany('INSERT INTO Courses VALUES (?, ?, ?)', courses_data)


#TEESRI TABLE BNA RHE - ENROLLMENT
cur.execute('''
    CREATE TABLE IF NOT EXISTS Enrollment (
        enrollment_id INTEGER PRIMARY KEY,
        rollno INTEGER,
        course_id INTEGER,
        semester TEXT,
        FOREIGN KEY (rollno) REFERENCES Students(rollno),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
''')

print("Table- Enrollment created successfully")
print("\n")

enrollment_data = [
    (1, 101, 1, 'Spring 2023'),
    (2, 102, 1, 'Spring 2023'),
    (3, 103, 1, 'Spring 2023'),
    (4, 104, 2, 'Spring 2023'),
    (5, 105, 2, 'Spring 2023'),
    (6, 106, 1, 'Fall 2023'),
    (7, 107, 1, 'Fall 2023'),
    (8, 108, 1, 'Fall 2023'),
    (9, 108, 2, 'Spring 2023'),
    (10, 110, 2, 'Fall 2023'),
    # Add more enrollment data here
]

cur.executemany('INSERT INTO Enrollment VALUES (?, ?, ?, ?)', enrollment_data)

conn.commit()



# Query 1: List students enrolled in "Computer Science (101)"

cur.execute('''
    SELECT Students.name
    FROM Students
    JOIN Enrollment ON Students.rollno = Enrollment.rollno
    JOIN Courses ON Enrollment.course_id = Courses.course_id
    WHERE Courses.course_name = 'Computer Science (101)'
''')

enrolled_students = cur.fetchall()
print("Students enrolled in 'Computer Science (101)':")
for student in enrolled_students:
    print(student[0])

print("\n")


#query 2- Find courses and instructors for student with roll number 103
cur.execute('''
    SELECT Courses.course_name, Courses.instructor
    FROM Courses
    JOIN Enrollment ON Courses.course_id = Enrollment.course_id
    WHERE Enrollment.rollno = 103
''')

courses_for_student_103 = cur.fetchall()
print("\nCourses and instructors for student with roll number 103:")
for course in courses_for_student_103:
    print(f"Course: {course[0]}, Instructor: {course[1]}")

print("\n")

conn.commit()

# Query to retrieve students not enrolled in any courses in the current semester(Fall Semester)
cur.execute('''
    SELECT Students.name
    FROM Students
    WHERE Students.rollno NOT IN (
        SELECT Enrollment.rollno
        FROM Enrollment
        WHERE Enrollment.semester = 'Fall 2023'
    )
''')

students_not_enrolled = cur.fetchall()
print("Students who have not enrolled in any courses in Fall 2023:")
for student in students_not_enrolled:
    print(student[0])

print("\n")

# Query to list students enrolled in at least two courses
cur.execute('''
    SELECT Students.name
    FROM Students
    WHERE Students.rollno IN (
        SELECT Enrollment.rollno
        FROM Enrollment
        GROUP BY Enrollment.rollno
        HAVING COUNT(Enrollment.course_id) >= 2
    )
''')

students_enrolled_in_at_least_two_courses = cur.fetchall()
print("Students enrolled in at least two courses:")
for student in students_enrolled_in_at_least_two_courses:
    print(student[0])

print("\n")

# Query to find the number of students enrolled in each course for Spring 2023
cur.execute('''
    SELECT Courses.course_name, Courses.instructor, COUNT(Enrollment.rollno) AS enrolled_students
    FROM Courses
    LEFT JOIN Enrollment ON Courses.course_id = Enrollment.course_id
    WHERE Enrollment.semester = 'Spring 2023'
    GROUP BY Courses.course_name, Courses.instructor
''')

enrollment_info = cur.fetchall()
print("Course Name | Instructor Name | Enrolled Students")
print("-" * 50)
for course in enrollment_info:
    print(f"{course[0]} | {course[1]} | {course[2]}")

print("\n")

# Query to count the number of students who have failed in at least one course

query = """
SELECT COUNT(DISTINCT Students.rollno)
FROM Students
JOIN Enrollment ON Students.rollno = Enrollment.rollno
WHERE Students.grade = 'F'
"""


# Execute the query and fetch the result
cur.execute(query)
result = cur.fetchall()

# Print the result
print("Number of students who have failed in at least one course:", result[0][0])

print("\n")



# print("\n")

# Query to list names and grades of students in courses taught by a specific instructor
cur.execute('''
    SELECT Students.name, Students.grade
    FROM Students
    JOIN Enrollment ON Students.rollno = Enrollment.rollno
    JOIN Courses ON Enrollment.course_id = Courses.course_id
    WHERE Courses.instructor = 'Dr. Blue'
''')

students_and_grades = cur.fetchall()
print("Students and their grades in courses taught by 'Dr. Blue':")
for student in students_and_grades:
    print(f"Name: {student[0]}, Grade: {student[1]}")

print("\n")

# Query to find unenrolled courses for the current semester
cur.execute('''
    SELECT Courses.course_name, Courses.instructor
    FROM Courses
    WHERE Courses.course_id NOT IN (
        SELECT DISTINCT Enrollment.course_id
        FROM Enrollment
        WHERE Enrollment.semester = 'Fall 2023'
    )
''')

unenrolled_courses = cur.fetchall()
print("Unenrolled courses for 'Fall 2023':")
for course in unenrolled_courses:
    print(f"Course Name: {course[0]}, Instructor: {course[1]}")

conn.close()
