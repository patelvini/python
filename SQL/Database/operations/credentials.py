import pyodbc

# server = 'CS79-PC\\SQLEXPRESS'
# database = 'DEMO'
# username = 'vini.patel'
# password = 'vini@123'
# DATABASE='+self.__database_name+';\

class Credentials:

	def selectServerHost(self,server_host):
		self.__server_host = server_host

	def selectUsername(self,username):
		self.__username = username

	def selectPassword(self,password):
		self.__password = password

	



