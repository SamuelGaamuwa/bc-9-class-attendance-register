from database_connections import database_insert_class
from database_connections import database_delete_class
from database_connections import database_return_classes

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

	#method to push class parameters to the database
	def register_class(self):
		database_insert_class(self.name, self.subject, self.teacher)

	#method to delete class parameters from the database
	@staticmethod
	def delete_class(class_id):
		database_delete_class(class_id)

	#method to list all the classes in the database
	@staticmethod
	def list_all_classes():
		class_list = database_return_classes()
		print("{} {} {}".format('Class Id'.ljust(15), 'Name'.ljust(20), 'Subject'.ljust(20), 'Teacher'.ljust(20)))
		print("=" * 50 )
		for row in class_list:
			print("{} {} {}".format(str(row[0]).ljust(15), row[1].ljust(20), row[2].ljust(20), row[3].ljust(20)))

