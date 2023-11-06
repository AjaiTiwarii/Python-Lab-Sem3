import sqlite3

conn = sqlite3.connect('students.db')
cur = conn.cursor()

print("Opened database successfully")

cur.execute("DROP TABLE IF EXISTS studentData")

cur.execute(''' CREATE TABLE IF NOT EXISTS studentData
        (rollno INT,
        name TEXT,
        phoneno INT,
        grade CHAR(2));''')

print("Table created successfully")


cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(101,'Ajay',9199,'EX'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(102,'Aman',8719,'B'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(103,'Ayushui',7824,'B'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(104,'Chirag',8731,'C'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(105,'Akash',7865,'D'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(110,'Kunal',9314,'A'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(106,'Saurabh',7317,'F'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(107,'Prakhar',9521,'P'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(108,'Himanshu',3416,'P'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(109,'shreya',8965,'EX'))

cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",(110,'Kunal',9314,'A'))



#values print krr rhe

cur.execute("SELECT * from studentData")
data = cur.fetchall()

originalROLl = []
duplicate = []
for item in data:
    print(item)
print("\n")

#Duplicate entries nikal rhe
for item in data:
    if(item not in originalROLl):
        originalROLl.append(item)
    else:
        duplicate.append(item)

print("Duplicate are- ",set(duplicate))

print("\n Duplicate entries removed-")
for duplicateID in list(set(duplicate)):
    cur.execute(F"DELETE FROM studentData WHERE rollno = {duplicateID[0]}")
    cur.execute("INSERT INTO studentData (rollno,name,phoneno,grade) VALUES (?,?,?,?)",duplicateID)


cur.execute("SELECT * from studentData")
data = cur.fetchall()

for item in data:
    print(item)

print("\n")

#Sorting kr diya data
print("After sorting the data in desceding order")
cur.execute("SELECT * from studentData ORDER BY rollno DESC")
data = cur.fetchall()

for item in data:
    print(item)

print("\n")

#Counting ex
print("Counting of students who got EX")

count=0
for item in data:
    if(item[3]=="EX"):
        count+=1

print(f"{count} students got EX")

print("\n")

#New attribute
print("Adding a new attribute city")
cur.execute('''ALTER TABLE studentData
              ADD COLUMN CITY TEXT;''')

print("\n")

#Updating values to city attribute
cur.execute(f"UPDATE studentData SET CITY = 'mumbai' WHERE rollno = {101}")

cur.execute(f"UPDATE studentData SET CITY = 'una' WHERE rollno = {102}")

cur.execute(f"UPDATE studentData SET CITY = 'raipur' WHERE rollno = {103}")

cur.execute(f"UPDATE studentData SET CITY = 'lucknow' WHERE rollno = {104}")

cur.execute(f"UPDATE studentData SET CITY = 'unnao' WHERE rollno = {105}")

cur.execute(f"UPDATE studentData SET CITY = 'jhansi' WHERE rollno = {106}")

cur.execute(f"UPDATE studentData SET CITY = 'noida' WHERE rollno = {107}")

cur.execute(f"UPDATE studentData SET CITY = 'Hyderabad' WHERE rollno = {108}")

cur.execute(f"UPDATE studentData SET CITY = 'Ahmedabad' WHERE rollno = {109}")

cur.execute(f"UPDATE studentData SET CITY = 'surat' WHERE rollno = {110}")

cur.execute("SELECT * from studentData")
data = cur.fetchall()

for item in data:
    print(item)

print("\n")

#Shifting students 101 to Kanpur
print("Shifting student with roll 101 to Kanpur")
print("\n")

cur.execute(f"UPDATE studentData SET CITY = 'Kanpur' WHERE rollno = {101}")

cur.execute("SELECT * from studentData")
data = cur.fetchall()

for item in data:
    print(item)

conn.commit()
conn.close()