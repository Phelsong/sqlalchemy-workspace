import sqlalchemy as db #

engine = db.create_engine('sqlite:///cameras.sqlite3')
connection = engine.connect()
metadata = db.MetaData()

cameras = db.Table('Cameras', metadata, autoload=True, autoload_with=engine)

query = db.select([cameras])
query2 = db.select([cameras]).where(cameras.columns.Brand == 'RED')

result_proxy = connection.execute (query2)
result_set = result_proxy.fetchall()

print(result_set[0])

query3 = cameras.insert().values(Brand="RED", Model="V-Raptor", Format="FF")
connection.execute (query3)

query4 = db.select([cameras])
result_proxy2 = connection.execute (query4)
result_set = result_proxy2.fetchall()
print(result_set[:4])