from datetime import datetime

from database_connect import database_insert_reason
from database_connect import database_return_reasons
from database_connect import database_insert_ongoing
from database_connect import database_return_ongoing
from database_connect import database_delete_ongoing
from database_connect import database_insert_inclass
from database_connect import database_return_inclass
from database_connect import database_delete_inclass
from database_connect import database_return_classes
from database_connect import database_return_students
from database_connect import database_delete_class_students

"""This is the attendance register and it contains functions or methods
to initiate and stop classes as well as checking students in and out of 
classes. It also passes relevant data to database_connection module
"""
class AttendanceRegister(object):

	def __init__():
		pass

	 
	@staticmethod
	def log_start(class_id):
	#method to log in a class if not logged in
		time = datetime.now()
		if class_id in database_return_ongoing():
			return "Class already logged in"
		for dataset in database_return_classes():
			if class_id in dataset:
				print(class_id)
				database_insert_ongoing(class_id, time)
				return "Class of id: {}, logged in".format(class_id)
		return "Class not created yet"
		
	@staticmethod
	def log_end(class_id):
	#method to log out a class if it is logged in 
		if class_id in database_return_ongoing():
			database_delete_ongoing(class_id)
			database_delete_class_students(class_id)
			return "Class has been logged out"
		return "Class is not on going"


	@staticmethod
	def check_in(student_id, class_id):
	#method to check student into a particular class
		if student_id in database_return_inclass():
			return "Student already attending class"
		for dataset in database_return_students():
			if student_id in dataset:
				print(student_id)
				database_insert_inclass(student_id, class_id)
				return "Student ID: {} checked into class ID: {}".format(student_id, class_id)
		return "Student not created yet"

 
	@staticmethod
	#method to check out student from a class
	def check_out(student_id, class_id, reason):
		day = datetime.now()
		database_delete_inclass(student_id, class_id)
		database_insert_reason(student_id, class_id, day, reason)
		return "Student ID: {} has been checked out".format(student_id)

	@staticmethod
	def show_reasons():
		print(database_return_reasons())

#AttendanceRegister.check_in(1, 2)

#print(AttendanceRegister.check_out(1, 2, "sick"))