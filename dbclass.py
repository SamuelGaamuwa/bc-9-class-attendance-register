import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Student(Base):
	__tablename__ = 'students'
	id = Column(Integer, primary_key=True, autoincrement=True)
	first_name = Column(String(250), nullable=False)
	last_name = Column(String(250), nullable=True ) 

class Classes(Base):
	__tablename__ = 'classes'
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String(250), nullable=False)
	subject = Column(String(250), nullable=False)
	teacher = Column(String(250), nullable=True)

class Reasons(Base):
	__tablename__ = 'reasons'
	id = Column(Integer, primary_key=True, autoincrement=True)
	student_id = Column(Integer, nullable=False)
	class_id = Column(Integer, nullable=True)
	day = Column(String(250), nullable=True)
	reason = Column(String(400), nullable=False)

class Ongoing(Base):
	__tablename__ ='ongoing'
	id = Column(Integer, primary_key=True, autoincrement=True)
	class_id = Column(Integer, nullable=False)
	ctime = Column(String(250), nullable=True)

class Inclass(Base):
	__tablename__ = 'inclass'
	id = Column(Integer, primary_key=True, autoincrement=True)
	class_id = Column(Integer, nullable=False)
	student_id = Column(Integer, nullable=False)

engine = create_engine('sqlite:///class_attendance_db')

Base.metadata.create_all(engine)
