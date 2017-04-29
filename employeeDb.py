class employeeDb(object):

#Initialize our DAO class with the database and set the MongoDB collection we want to use
	def __init__(self, database):
		self.db = database
		self.mynames = database.employees

#This function will handle the finding of names
	def find_names(self):
		l = []
		for each_name in self.mynames.find():
			l.append({'name':each_name['name'], 'salary':each_name['salary']})

		return l
	def stats(self):
		salaries = []
		for s in self.mynames.find():
			salaries.append({'salary':s["salary"]})
		return salaries

#This function will handle the insertion of names
	def insert_name(self,newname,newsalary):
		newname = {'name':newname,'salary':newsalary}
		self.mynames.insert(newname)
	def delete_name(self,delname):
		self.mynames.delete_many({"name":delname})
	def delete_all(self,delall=None):
		self.mynames.delete_many({})
	def update_name(self,updatename,updatesalary):
		self.mynames.update(
		  { "name" : updatename },
		  { "$set": { "salary": updatesalary } }
		)