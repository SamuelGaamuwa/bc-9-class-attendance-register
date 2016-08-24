import sqlite3

conn = sqlite3.connect("class_attendance_db" )
"""
conn.execute('''CREATE TABLE students
       (id 			INTEGER 	PRIMARY KEY AUTOINCREMENT  NOT NULL,
       first_name   TEXT 	NOT NULL,
       last_name    TEXT   	NOT NULL );''') 

conn.execute('''CREATE TABLE classes
       (id 			INTEGER 	PRIMARY KEY  AUTOINCREMENT  NOT NULL,
       name   		TEXT 	NOT NULL,
       subject		TEXT 	NOT NULL,
       teacher    	TEXT   	NOT NULL );''')

conn.execute('''CREATE TABLE reasons
       (id 			INTEGER 	PRIMARY KEY  AUTOINCREMENT  NOT NULL,
       student_id	INTEGER 	NOT NULL,
       class_id		INTEGER 	NOT NULL,
       day			TEXT	NOT NULL,
       reason    	TEXT   	NOT NULL );''')

conn.execute('''CREATE TABLE ongoing
       (class_id	INTEGER 	NOT NULL,
       ctime		TEXT	NOT NULL);''')

conn.execute('''CREATE TABLE inclass
       (class_id	INTEGER 	NOT NULL,
       student_id	INTEGER		NOT NULL);''')
"""

def database_insert_student(first_name, last_name):
#function to insert students into the database
	sql = "INSERT INTO students(first_name, last_name) VALUES ('{}', '{}')".format(first_name, last_name)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_insert_class(name, subject, teacher):
#function to insert classes into the database
	sql = "INSERT INTO classes(name, subject, teacher) VALUES ('{}', '{}', '{}')".format(name, subject, teacher)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_insert_reason(student_id, class_id, day, reason):
#function to enter reasons for student's checkout
	sql = "INSERT INTO reasons(student_id, class_id, day, reason) VALUES ('{}', '{}', '{}', '{}')".format(student_id, class_id, day, reason)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()

def database_insert_ongoing(class_id, ctime):
#function to insert data on ongoing classes into the database
	sql = "INSERT INTO ongoing(class_id, ctime) VALUES ('{}', '{}')".format(class_id, ctime)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()

def database_insert_inclass(student_id, class_id):
#function to insert data on students in class into the database
	sql = "INSERT INTO inclass(class_id, student_id) VALUES ('{}', '{}')".format(class_id, student_id)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()

def database_delete_student(student_id):
#function to delete student from the database
	sql = "DELETE FROM students WHERE id = {};".format( str(student_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_delete_class(class_id):
#function to delete class from the database
	sql = "DELETE FROM classes WHERE id = {};".format( str(class_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_delete_ongoing(class_id):
#function to delete ongoing classes from the database
	sql = "DELETE FROM ongoing WHERE class_id = {};".format( str(class_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_delete_inclass(student_id):
#function to delete students in class from the database
	sql = "DELETE FROM inclass WHERE student_id = {};".format( str(student_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

def database_return_students():
#function to return students from the database
	cursor = conn.execute("SELECT * FROM students")
	new = cursor.fetchall()
	return new

def database_return_ongoing():
#function to return ongoing classes from the database
	cursor = conn.execute("SELECT class_id FROM ongoing")
	new = cursor.fetchall()
	value_list = []
	for num in range(len(new) ):
		value_list.append(new[num][0])
	return value_list

def database_return_inclass():
#function to return students in class from the database
	cursor = conn.execute("SELECT student_id FROM inclass")
	new = cursor.fetchall()
	#return new
	value_list = []
	for num in range(len(new)):
		value_list.append(new[num][0])
	return value_list

def database_return_classes():
#function to return classes from the database
	cursor = conn.execute("SELECT * FROM classes")
	new = cursor.fetchall()
	return new

def database_return_reasons():
#function to return the reasons for leaving class 
	cursor = conn.execute("SELECT * FROM reasons")
	new = cursor.fetchall()
	return new

#print(database_return_inclass())