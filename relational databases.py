#Relational databases 1.postgreSQL, 2.mySQL, 3.SQLite, 4.SQL(structure quriy language)
#SQLite
from sqlalchemy import create_engine
engine = create_engine('sqlite:///Chinook.sqlite')
table_names = engine.table_names()
print(table_names)

