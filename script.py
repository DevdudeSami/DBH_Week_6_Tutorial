## imports
from peewee import *

## set up models / task 3
schools_db = SqliteDatabase('data.db')

class School(Model):
	class Meta:
		database = schools_db
		table_name = 'schools'		
		

	dbn = CharField(unique=True, null=False, primary_key=True)
	school_name = CharField(null=False)
	number_of_test_takers = IntegerField(null=False)
	critical_reading_mean = IntegerField(null=False)
	mathematics_mean = IntegerField(null=False)
	writing_mean = IntegerField(null=False)


#------------
## task 4
#------------
### 1
requiredSchool = School.get(School.dbn == '01M292')
print("(4,1) The school with the required dbn is " + requiredSchool.school_name + ".")
### 2
schoolsWithMoreThan500Students = School.select().where(School.number_of_test_takers > 500)
print("(4,2) There are " + str(schoolsWithMoreThan500Students.count()) + " that have more than 500 students taking the test.")
### 3
print("(4,3) The schools that have more than 500 students are: ")
for school in schoolsWithMoreThan500Students:
	print("\t - " + school.school_name)
### 4
schoolsWithMoreThan50Students = School.select().where(School.number_of_test_takers > 50).order_by(School.mathematics_mean.desc())[0:5]
print("(4,4) The first 5 schools that have more than 50 students are sorted descendingly by mathematics score mean: ")
for school in schoolsWithMoreThan50Students:
	print("\t - " + school.school_name + " | " + str(school.mathematics_mean))

#------------
## task 5
#------------
### Part 1
students_db = SqliteDatabase('student.db')
### Part 2
class Student(Model):
	class Meta:
		database = students_db
		table_name = 'student'

	username = CharField(unique = True, null = False, primary_key = True, max_length = 255)
	score = IntegerField(null = False)


