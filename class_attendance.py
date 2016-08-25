import click

from student import Student  
from classes import Class
from attendance_register import AttendanceRegister


"""
	This is the Class Attendance Register, it has various commands allowing users
	to execute commands.
	register, to enter and save class and student information in the database
	delete, to remove specific class and student information from the database
	list, to return a list of all the classes and students in the database
	log, to start and end classes 
	check, to check students in and out of classes
"""

@click.group()
def cli():
	pass

@cli.command()
@click.option('--add',  nargs=2 , type=str, help="Enter a student's <first name> and <last name> to add them")
@click.option('--remove', type=int, help="Deletes a student from the database by their id <studentID>")
@click.option('--display', is_flag=True, help="Lists all the students in the database")
def student(add, remove, display):
	if len(add) != 0:
		stu = Student(add[0], add[1])
		stu.register_student()
	elif remove is not None:
		print(Student.delete_student(remove))
	elif display:
		Student.list_students()

@cli.command()
@click.option('--add', nargs=3, help="Enter class <name> <subject> <teacher> to add class")
@click.option('--remove', type=int, help="Deletes a class from the database by its id <classID>")
@click.option('--display', is_flag=True, help="Lists all the classes in the database")
def classes(add, remove, display):
	if len(add) != 0:
		cla = Class(add[0], add[1], add[2])
		cla.register_class()
	elif remove is not None:
		Class.delete_class(remove) 
	elif display:
		Class.list_all_classes()

@cli.command()
@click.option('--start', type=int, help="Starts a class by its id <classID>")
@click.option('--end', type=int, help="Ends a class by its id <classID>")
def log(start, end):
	if start is not None:
		print(AttendanceRegister.log_start(start))
	if end is not None:
		print(AttendanceRegister.log_end(end))

@cli.command()
@click.option('--into', nargs=2, type=int, help="checks a student into a class using the respective IDs <studentID> <classID>")
@click.option('--out', nargs=3, help="checks a student out of a class using IDs and takes a reason <studentID> <classID> <reason>")
def check(into, out):
	if len(into) != 0:
		print(AttendanceRegister.check_in(into[0], into[1]))
	if len(out) != 0:
		print(AttendanceRegister.check_out(out[0], out[1], out[2]))

@cli.command()
@click.option('--display', is_flag=True, help="Lists all the students that were checked out of class and reasons why")
def reason(display):
	if display:
		AttendanceRegister.show_reasons()

if __name__ == '__main__':
	cli()
