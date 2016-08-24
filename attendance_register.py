from datetime import datetime
class AttendanceRegister(object):
	attending_list = []
	on_going_classes = []
	class_students = []

	def __init__():

	#method to log in a class if not logged in 
	@staticmethod
	def log_start(class_id):
		time = datetime.now()
		for item in on_going_classes:
			for value in item.keys():
				if class_id == value:
					return "Class already logged in"
		on_going_classes.append({class_id: time})
		class_students.append({class_id: []})
		return "Class of id: {}, logged in".format(class_id)
		
	#method to log out a class if it is logged in 
	@staticmethod
	def log_end(class_id):
		for item in on_going_classes:
			for value in item.keys():
				if class_id == value:
					on_going_classes.pop(on_going_classes.index(item))
					return "Class has been logged out"
		return "Class is not on going"

	#method to check student into a particular class
	@staticmethod
	def check_in(student_id, class_id):
		for student in attending_list:
			if student == student_id:
				return "Student already attending class"
		for item in on_going_classes:
			for value in item.keys():
				if class_id == value:
					for element in class_students:
						for key in element.keys():
							if key == class_id:
								element[class_id].append(student_id)
								attending_list.append(student_id)

	#method to check out student from a class 
	@staticmethod
	def check_out(student_id, class_id, reason):
		day = datetime.date.now()
		for student in attending_list:
			if student == student_id:
				for element in class_students:
					for key in element.keys():
						if key == class_id:
							element[class_id].pop(element[class_id].index(student_id))
							return "Student has been checked out"
		return "Student not attending a class"
