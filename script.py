## imports
from peewee import *

## set up models / task 3
db = SqliteDatabase('data.db')

class BaseModel(Model):
    class Meta:
        database = db

class School(BaseModel):
	class Meta:
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
