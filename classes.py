from database_connections import database_insert_class
from database_connections import database_delete_class
from database_connections import database_return_classes
from database_connections import database_return_ongoing
from database_connections import database_students_per_class

class Class(object):
	'''
		This is class for the Classes and the operations on them,
		including, the creation and registration of new class and 
		addition to the database, the deletion of classes from the database as well
	'''

	def __init__(self, name, subject, teacher):
		self.name = name
		self.teacher = teacher
		self.subject = subject

	def register_class(self):
		database_insert_class(self.name, self.subject, self.teacher)

	@staticmethod
	def delete_class(class_id):
		database_delete_class(class_id)

	@staticmethod
	def list_all_classes():
		print("{} {} {} {} {} {}".format('Class Id'.ljust(10), 'Name'.ljust(15), 'Subject'.ljust(15), 'Teacher'.ljust(15), 'Status'.ljust(10), 'Present'.ljust(10)))
		print("=" * 75 )
		for row in database_return_classes():
			status = 'In Recess'
			present = '0'
			if row[0] in database_return_ongoing():
				status = 'On Going'
				present = database_students_per_class(row[0])
			print("{} {} {} {} {} {}".format(str(row[0]).ljust(10), row[1].ljust(15), row[2].ljust(15), row[3].ljust(15), status.ljust(10), present.ljust(10)))

