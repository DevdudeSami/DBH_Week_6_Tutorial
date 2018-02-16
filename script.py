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
