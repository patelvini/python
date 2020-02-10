import demo_connection as dc

# dc = dc.DemoConnection(input("Enter database name : "))

# dc.selectServerHost(input("Enter server host name : "))
# dc.selectUsername(input("Enter user name : "))
# dc.selectPassword(input("Enter password : "))
# dc.createConnection()
# dc.createTable(input("Enter table name : "))

class Operation:

	def switch_demo(self,argument):
		func = switcher.get(argument, "Invalid choice !!!")
		return func

	def insertData(self):
		p_name = input("Enter product name : ")
		price = input("Enter price : ")

		cr.execute("INSERT INTO PRODUCT (PRODUCT_NAME,PRICE) VALUES (?,?)",(p_name,price))
		db.conn.commit()
		print("Inserted Successfully !!\n")

		# return self.insert_data
	def readData(self):
		table_name = input("Enter table name : ")
		self.res = cr.execute("SELECT * FROM "+table_name)
		for row in self.res:
			print(row)

		db.conn.commit()

	# def updateData(self):
	# 	table_name = input("Enter table name : ")
	# 	id = input("Enter id for search : ")

if __name__ == '__main__':

	op = Operation()
	db = dc.DemoConnection('DEMO')

	db.selectServerHost('CS79-PC\\SQLEXPRESS')
	db.selectUsername('vini.patel')
	db.selectPassword('vini@123')
	cr = db.createConnection()

	print("1 : for Insert in table")
	print("2 : for Read data from table")

	ch = int(input("Enter your choice : "))

	switcher = {1: op.insertData,2: op.readData}
	
	op.switch_demo(ch)
	


