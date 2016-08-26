import click

from pyfiglet import Figlet
from colorama import Fore
from colorama import Back
from colorama import Style
from colorama import init

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
@click.option('--add',  is_flag=True, help="Enter a student's <first name> and <last name> to add them")
@click.option('--remove', is_flag=True, help="Deletes a student from the database by their id <studentID>")
@click.option('--display', is_flag=True, help="Lists all the students in the database")
def student(add, remove, display):
	if add:
		first_name = input("Student's first name: ")
		second_name = input("Student's last name: ")
		stu = Student(first_name, second_name)
		stu.register_student()
	elif remove:
		student_id = input("Enter Student's Id: ")
		print(Student.delete_student(student_id))
	elif display:
		Student.list_students()

@cli.command()
@click.option('--add', is_flag=True, help="Enter class <name> <subject> <teacher> to add class")
@click.option('--remove', is_flag=True, help="Deletes a class from the database by its id <classID>")
@click.option('--display', is_flag=True, help="Lists all the classes in the database")
def classes(add, remove, display):
	if add:
		class_name = input("Enter the Class Name: ")
		subject = input("Enter the Class Subject: ")
		teacher = input("Enter the Teacher's Name: ")
		cla = Class(class_name, subject, teacher)
		cla.register_class()
	elif remove:
		class_id = input("Enter Class' Id: ")
		Class.delete_class(class_id) 
	elif display:
		Class.list_all_classes()

@cli.command()
@click.option('--start', is_flag=True, help="Starts a class by its id <classID>")
@click.option('--end', is_flag=True, help="Ends a class by its id <classID>")
def log(start, end):
	if start:
		class_id = input("Enter Class Id to start class: ")
		print(AttendanceRegister.log_start(int(class_id)))
	if end:
		class_id = input("Enter Class Id to end class: ")
		print(AttendanceRegister.log_end(int(class_id)))

@cli.command()
@click.option('--into', is_flag=True, help="checks a student into a class using the respective IDs <studentID> <classID>")
@click.option('--out', is_flag=True, help="checks a student out of a class using IDs and takes a reason <studentID> <classID> <reason>")
def check(into, out):
	if into:
		student_id = input("Enter the Student's id: ")
		class_id = input("Enter the Class' id: ")
		print(AttendanceRegister.check_in(int(student_id), int(class_id)))
	if out:
		student_id = input("Enter the Student's id: ")
		class_id = input("Enter the Class' id: ")
		reason = input("Enter a reason for check out: ")
		print(AttendanceRegister.check_out(int(student_id), int(class_id), reason))

@cli.command()
@click.option('--display', is_flag=True, help="Lists all the students that were checked out of class and reasons why")
def reason(display):
	if display:
		AttendanceRegister.show_reasons()

@cli.command()
def start():
	init(autoreset=True)
	font = Figlet(font='doubleshorts')
	print(Fore.CYAN +font.renderText("CLASS ATTENDANCE REGISTER"))
	print("="*60)
	print(Fore.YELLOW + "\nWelcome to Class Attendance Register, a few commands below to help you on your way\n\n")
	print("student: For operations on students including, adding and removing students, and listing all students\n")
	print("classes: For operations on classes including, adding and removing classes, and listing all classes\n")
	print("log: For logging the start and end of classes\n")
	print("check: For checking students in and out of classes\n")
	print("reason: For displaying students that were checked out of class for various reasons\n\n")
	print(Fore.YELLOW + "FOR MORE INFORMATION ON EACH COMMAND USE class_attendance <command> --help")

if __name__ == '__main__':
	cli()
