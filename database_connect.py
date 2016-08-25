from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dbclass import Classes 
from dbclass import Student 
from dbclass import Reasons
from dbclass import Ongoing
from dbclass import Inclass

engine = create_engine('sqlite:///class_attendance_db')

Base = declarative_base()

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

def database_insert_student(fname, lname):
	new_student = Student(first_name=fname, last_name=lname)
	session.add(new_student)
	session.commit()

def database_insert_class(cname, csubject, cteacher):
	new_class = Classes(name=cname, subject=csubject, teacher=cteacher)
	session.add(new_class)
	session.commit()

def database_insert_reason(rstudent_id, rclass_id, rday, rreason):
	new_reason = Reasons(student_id=rstudent_id, class_id=rclass_id, day=rday, reason=rreason)
	session.add(new_reason)
	session.commit()

def database_insert_ongoing(oclass_id, octime):
	new_ongoing = Ongoing(class_id=oclass_id, ctime=octime)
	session.add(new_ongoing)
	session.commit()

def database_insert_inclass(istudent_id, iclass_id):
	new_inclass = Inclass(student_id=istudent_id, class_id=iclass_id)
	session.add(new_inclass)
	session.commit()

def database_return_students():
	results = []
	rows = session.query(Student).all()
	for row in rows:
		results.append((row.id, row.first_name, row.last_name))
	return results

def database_return_classes():
	results = []
	rows = session.query(Classes).all()
	for row in rows:
		results.append((row.id, row.name, row.subject, row.teacher))
	return results

def database_return_ongoing():
	results = []
	rows = session.query(Ongoing).all()
	for row in rows:
		results.append(row.class_id)
	return results

def database_return_inclass():
	results = []
	rows = session.query(Inclass).all()
	for row in rows:
		results.append(row.student_id)
	return results

def database_return_reasons():
	results = []
	rows = session.query(Reasons).all()
	for row in rows:
		results.append((row.student_id, row.class_id, row.day, row.reason))
	return results

def database_students_per_class(class_id):
	rows = session.query(Inclass).all()
	count = 0
	for row in rows:
		if row.id == class_id:
			count = count + 1
	return count

def database_delete_student(student_id):
	session.query(Student).filter_by(id=student_id).delete()
	session.commit()

def database_delete_class(class_id):
	session.query(Classes).filter_by(id=class_id).delete()
	session.commit()

def database_delete_ongoing(oclass_id):
	session.query(Ongoing).filter_by(class_id=oclass_id).delete()
	session.commit()

def database_delete_inclass(istudent_id, iclass_id):
	session.query(Inclass).filter_by(student_id=istudent_id, class_id=iclass_id).delete()
	session.commit()

def database_delete_class_students(sclass_id):
	session.query(Inclass).filter_by(class_id=sclass_id).delete()
	session.commit()
