import pyodbc


# for driver in pyodbc.drivers():
# 	print(driver)

server = 'CS79-PC\\SQLEXPRESS'
database = 'DEMO'
username = 'vini.patel'
password = 'vini@123'


# define our connection string

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};\
	SERVER='+server+';\
	DATABASE='+database+';\
	UID='+username+';\
	PWD='+password+';\
	Trusted_Connection=yes;')

# creat the connection cursor

cursor  = conn.cursor()

# DEFINE SELECT QUERY

select_query = '''SELECT * FROM CUSTOMER'''

cursor.execute(select_query)

for row in cursor:
	print(row)

# define insert query

# insert_query = '''INSERT INTO CUSTOMER ([FIRST_NAME],[LAST_NAME],[CITY],[AGE])
# VALUES ('abc','XYZ','DJSDFSJKAHGFF',26);'''



