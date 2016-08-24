from student import Student  
from classes import Class
from attendance_register import AttendanceRegister
import click

"""
	This is the Class Attendance Register, providing users with the ability to 
	create classes and students, delete classes and students, list the classes 
	and students in the database. It also checks students in and out of classes, 
	as well as logging the start and end of the various classes
"""

@click.group()
def cli():
	pass

@cli.command()
@click.option('--student', nargs = 2 , type = str, help = "Enter a student's first and last name to register them")
@click.option('--clas', nargs = 3, type = str, help = "Enter the class' name, subject and teacher")
def register(clas, student):
#function to register students or a class, by passing the required arguments, should not have default 
	if len(student) != 0:
		stu = Student(student[0], student[1])
		stu.register_student()
	elif len(clas) != 0:
		cla = Class(clas[0], clas[1], clas[2])
		cla.register_class()
	else:
		print ("Enter parameters correctly")

@cli.command()
@click.option('--student', type = int, help = "Deletes a student from the database by their id <studentID>")
@click.option('--clas', type = int, help = "Deletes a class from the database by its id <classID>")
def delete(clas, student):
#function to delete a class or student from the database, should not have default
	if student is not None:
		Student.delete_student(student)
	elif clas is not None:
		Class.delete_class(clas) 

@cli.command()
@click.option('--students', is_flag = True, help = "Lists all the students in the database")
@click.option('--classes', is_flag = True, help= "Lists all the classes in the database")
def list(students, classes):
#function to list all the students or classes in the database
	if students:
		Student.list_students()
	if classes:
		Class.list_all_classes()

@cli.command()
@click.option('--start', type = int, help = "Starts a class by its id <classID>")
@click.option('--end', type = int, help = "Ends a class by its id <classID>")
def log(start, end):
#function to log both start and end for classes, should not have default
	if start is not None:
		print(AttendanceRegister.log_start(start))
	if end is not None:
		print(AttendanceRegister.log_end(end))

@cli.command()
@click.option('--into', nargs = 2, type = int, help = "checks a student into a class using the respective IDs <studentID> <classID>")
@click.option('--out', nargs = 3, help = "checks a student out of a class using IDs and takes a reason <studentID> <classID> <reason>")
def check(into, out):
#function to check students in and out of classes
	if len(into) != 0:
		print(AttendanceRegister.check_in(into[0], into[1]))
	if len(out) != 0:
		print(AttendanceRegister.check_out(out[0], out[1], out[2]))

if __name__ == '__main__':
	cli()
