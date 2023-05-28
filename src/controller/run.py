import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from model.db_model import bdd

db1 = bdd()

DB_NAME = "eshop"


db1.select_db(DB_NAME, force=True)

TABLES = {}
TABLES["client"] = ("""CREATE TABLE IF NOT EXISTS client (
	idClient INT AUTO_INCREMENT PRIMARY KEY,
    Cname VARCHAR(15),
    Csurname VARCHAR (45)
) ENGINE=InnoDB""")

db1.create_table(TABLES['client'])

cols = ("Cname", "Csurname")
data = ("Amanda", "Zanetti")

#print (f'{cols[0]}, {cols[1]}')

db1.insert_row("client", cols, data)

db1.cnx.commit()

print ("Sucess!")




