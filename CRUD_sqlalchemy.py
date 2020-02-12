import sqlalchemy as db

server = 'DESKTOP-IJLVEF5'
database = 'db1'
DRIVER = 'SQL Server'
username = 'patelvini136@gmail.com'
password = 'Avipatel@1226'
Database_Connection = f'mssql://{username}:{password}@{server}/{database}?driver={DRIVER}' 
engine = db.create_engine(Database_Connection)
connection = engine.connect()

metadata = db.MetaData()

result = db.Table('t1', metadata, autoload = True, autoload_with = engine)

print(result.columns.keys()) 
