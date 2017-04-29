import bottle
import pymongo
import employeeDb

salaries = []

@bottle.route('/')

def employeedata_index():
	mynames_list = employeedata.find_names()
	for x in mynames_list:
		salaries.append(int(x['salary']))
		avg = sum(salaries)/len(salaries)
		minima = min(salaries)
		maxima = max(salaries)
		mynames_list.append({'average':avg,'minima':minima,'maxima':maxima})
		#return mynames_list
	return bottle.template('index', dict(mynames = mynames_list))
@bottle.route('/newemployee', method='POST')
def insert_newemployee():
	name = bottle.request.forms.get("name")
	salary = bottle.request.forms.get("salary")
	employeedata.insert_name(name,salary)
	bottle.redirect('/')
@bottle.route('/delete' ,method = 'POST')
def delete_employee():
	delname = bottle.request.forms.get("delname")
	employeedata.delete_name(delname)
	bottle.redirect('/')
@bottle.route('/deleteall' ,method = 'POST')
def delete_all():
	employeedata.delete_all()
	bottle.redirect('/')
@bottle.route('/update', method = 'POST')
def update():
	updatename = bottle.request.forms.get("updatename")
	updatesalary = bottle.request.forms.get("updatesalary")
	employeedata.update_name(updatename,updatesalary)
	bottle.redirect('/')




#This is to setup the connection

#First, setup a connection string. My server is running on this computer so localhost is OK
connection_string = "mongodb://localhost"
#Next, let PyMongo know about the MongoDB connection we want to use.  PyMongo will manage the connection pool
connection = pymongo.MongoClient(connection_string)
#Now we want to set a context to the names database we created using the mongo interactive shell
database = connection.names
#Finally, let out data access object class we built which acts as our data layer know about this
employeedata = employeeDb.employeeDb(database)

bottle.debug(True)
bottle.run(host='localhost', port=8082) 

