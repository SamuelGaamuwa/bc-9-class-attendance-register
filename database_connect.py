from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from dbclass import Classes, Student, Reasons, Ongoing, Inclass

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

database_insert_student('samuel', 'gaamuwa')
print(database_return_students())