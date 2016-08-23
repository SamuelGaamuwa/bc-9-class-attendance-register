import sqlite3

conn = sqlite3.connect("class_attendance_db" )
 
conn.execute('''CREATE TABLE students
       (id 			INTEGER 	PRIMARY KEY AUTOINCREMENT  NOT NULL,
       first_name   TEXT 	NOT NULL,
       last_name    TEXT   	NOT NULL );''') 

conn.execute('''CREATE TABLE classes
       (id 			INTEGER 	PRIMARY KEY  AUTOINCREMENT  NOT NULL,
       name   		TEXT 	NOT NULL,
       subject		TEXT 	NOT NULL,
       teacher    	TEXT   	NOT NULL );''')


#function to insert students into the database
def database_insert_student(first_name, last_name):
	sql = "INSERT INTO students(first_name, last_name) VALUES ('{}', '{}')".format(first_name, last_name)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

#function to insert classes into the database
def database_insert_class(name, subject, teacher):
	sql = "INSERT INTO classes(name, subject, teacher) VALUES ('{}', '{}', '{}')".format(name, subject, teacher)
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

#function to delete student from the database
def database_delete_student(student_id):
	sql = "DELETE FROM students WHERE id = {};".format( str(student_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

#function to delete class from the database
def database_delete_class(class_id):
	sql = "DELETE FROM classes WHERE id = {};".format( str(class_id))
	try:
		conn.execute(sql)
		conn.commit()
	except:
		conn.rollback()
	#conn.close()

#function to return students from the database
def database_return_students():
	cursor = conn.execute("SELECT * FROM students")
	new = cursor.fetchall()
	return new

#function to return classes from the database
def database_return_classes():
	cursor = conn.execute("SELECT * FROM classes")
	new = cursor.fetchall()
	return new
