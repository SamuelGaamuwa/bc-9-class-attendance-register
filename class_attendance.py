from student import Student  
from classes import Class
import click

@click.group()
def cli():
	pass

@cli.command()
@click.option('--student', nargs = 2 , type = str, help = "Enter a student's first and last name to register them")
@click.option('--clas', nargs = 3, type = str, help = "Enter the class' name, subject and teacher")
def register(clas, student):
	if len(student) != 0:
		stu = Student(student[0], student[1])
		stu.register_student()
	elif len(clas) != 0:
		cla = Class(clas[0], clas[1], clas[2])
		cla.register_class()
	else:
		print ("Enter parameters correctly")

@cli.command()
@click.option('--student', default = None)
@click.option('--clas', default = None)
def delete(clas, student):
	if student is not None:
		Student.delete_student(student)
	elif clas is not None:
		Class.delete_class(clas) 

@cli.command()
@click.option('--students', is_flag = True)
@click.option('--classes', is_flag = True)
def list(students, classes):
	if students:
		Student.list_students()
	if classes:
		Class.list_all_classes()



if __name__ == '__main__':
	cli()
