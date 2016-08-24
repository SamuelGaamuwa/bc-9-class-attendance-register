from database_connections import database_insert_student
from database_connections import database_return_students
from database_connections import database_delete_student
from database_connections import database_return_inclass


class Student(object):
	"""
		This is the student class, it is supposed to take care of student operations,
		like registering the student and deleting students
	"""
	def __init__(self, first_name, last_name):
		self.first_name = first_name
		self.last_name = last_name

	def register_student(self):
	#send the information collected to the database
		database_insert_student(self.first_name, self.last_name)

	@staticmethod
	def delete_student(student_id):
	#pass information of student to be deleted from the database
		database_delete_student(student_id)

	@staticmethod
	def list_students():
	#method to list all students in the database 
		print("{} {} {} {}".format('Student Id'.ljust(15), 'First Name'.ljust(20), 'Last Name'.ljust(20), 'Status'.ljust(15)))
		print("=" * 75 )
		for row in database_return_students():
			status = 'Not In Class'
			if row[0] in database_return_inclass():
				status = 'In Class'
			print("{} {} {} {}".format(str(row[0]).ljust(15), row[1].ljust(20), row[2].ljust(20), status.ljust(15)))
				