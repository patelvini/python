import demo_connection as dc

class Operation:

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

	def createTable(self):
		table_name = input("Enter table name : ")

		query = "CREATE TABLE "+table_name+"(ID INT PRIMARY KEY IDENTITY (1,1), "

		while True:
			colname=input("Enter column name, exit to stop adding columns : ")
			if colname=="exit":
				query+=");"
				break
			dtype=input("Enter column data type: INT,CHAR OR VARCHAR : ")
			if dtype=="INT":
				query+=colname+" "+dtype+", "
			else:
				size=input("Enter size for column : ")
				query+=colname+" "+dtype+" ("+size+"), "

		cr.execute(query)
		db.conn.commit()

		print("Table created Successfully !!")

	# def updateData(self):
	# 	table_name = input("Enter table name : ")
	# 	id = input("Enter id for search : ")

if __name__ == '__main__':

	op = Operation()
	db = dc.DemoConnection('DEMO')

	db.selectServerHost('CS79-PC\\SQLEXPRESS')
	db.selectUsername('vini.patel')
	db.selectPassword('vini@123')
	# db = dc.DemoConnection(input("Enter database name : "))

	# db.selectServerHost(input("Enter server host name : "))
	# db.selectUsername(input("Enter user name : "))
	# db.selectPassword(input("Enter password : "))

	cr = db.createConnection()

	op.createTable()


	


