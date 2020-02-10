from operations import *

op = CRUD_Operation()
db = DemoConnection('DEMO')
cd = Credentials()

cd.selectServerHost('CS79-PC\\SQLEXPRESS')
cd.selectUsername('vini.patel')
cd.selectPassword('vini@123')
cr = db.createConnection()

	# op.insertData()
op.readData()