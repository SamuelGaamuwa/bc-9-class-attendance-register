from datetime import datetime
from database_connections import database_insert_reason
from database_connections import database_return_reasons


class AttendanceRegister(object):
	attending_list = []
	on_going_classes = []
	class_students = []

	def __init__():
		pass

	#method to log in a class if not logged in 
	@staticmethod
	def log_start(class_id):
		time = datetime.now()
		for item in AttendanceRegister.on_going_classes:
			for value in item.keys():
				if class_id == value:
					return "Class already logged in"
		AttendanceRegister.on_going_classes.append({class_id: time})
		AttendanceRegister.class_students.append({class_id: []})
		return "Class of id: {}, logged in".format(class_id)
		
	#method to log out a class if it is logged in 
	@staticmethod
	def log_end(class_id):
		for item in AttendanceRegister.on_going_classes:
			for value in item.keys():
				if class_id == value:
					AttendanceRegister.on_going_classes.pop(AttendanceRegister.on_going_classes.index(item))
					return "Class has been logged out"
		return "Class is not on going"

	#method to check student into a particular class
	@staticmethod
	def check_in(student_id, class_id):
		for student in AttendanceRegister.attending_list:
			if student == student_id:
				return "Student already attending class"
		for item in AttendanceRegister.on_going_classes:
			for value in item.keys():
				if class_id == value:
					for element in AttendanceRegister.class_students:
						for key in element.keys():
							if key == class_id:
								element[class_id].append(student_id)
								AttendanceRegister.attending_list.append(student_id)
								return "Student ID: {} checked into class ID: {}".format(student_id, class_id)

	#method to check out student from a class 
	@staticmethod
	def check_out(student_id, class_id, reason):
		day = datetime.now()
		for student in AttendanceRegister.attending_list:
			if student == student_id:
				for element in AttendanceRegister.class_students:
					for key in element.keys():
						if key == class_id:
							element[class_id].pop(element[class_id].index(student_id))
							AttendanceRegister.attending_list.pop(AttendanceRegister.attending_list.index(student_id))
							database_insert_reason(student_id, class_id, day, reason)
							return "Student has been checked out"
		return "Student not attending a class"

	@staticmethod
	def show_reasons():
		print(database_return_reasons())


