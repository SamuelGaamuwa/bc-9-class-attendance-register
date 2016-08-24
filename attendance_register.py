from datetime import datetime
from database_connections import database_insert_reason
from database_connections import database_return_reasons
from database_connections import database_insert_ongoing
from database_connections import database_return_ongoing
from database_connections import database_delete_ongoing
from database_connections import database_insert_inclass
from database_connections import database_return_inclass
from database_connections import database_delete_inclass

class AttendanceRegister(object):
	attending_list = []
	on_going_classes = []
	class_students = []

	def __init__():
		pass

	 
	@staticmethod
	def log_start(class_id):
	#method to log in a class if not logged in
		time = datetime.now()
		if class_id in database_return_ongoing():
			return "Class already logged in"
		database_insert_ongoing(class_id, time)
		return "Class of id: {}, logged in".format(class_id)
		
	@staticmethod
	def log_end(class_id):
	#method to log out a class if it is logged in 
		if class_id in database_return_ongoing():
			database_delete_ongoing(class_id)
			return "Class has been logged out"
		return "Class is not on going"


	@staticmethod
	def check_in(student_id, class_id):
	#method to check student into a particular class
		if student_id in database_return_inclass():
			return "Student already attending class"
		database_insert_inclass(student_id, class_id)
		return "Student ID: {} checked into class ID: {}".format(student_id, class_id)

 
	@staticmethod
	#method to check out student from a class
	def check_out(student_id, class_id, reason):
		day = datetime.now()
		if student_id in database_return_inclass():
			database_delete_inclass(student_id)
			#database_insert_reason(student_id, class_id, day, reason)
			return "Student ID: {} has been checked out".format(student_id)
		return "Student not attending a class"

	@staticmethod
	def show_reasons():
		print(database_return_reasons())


