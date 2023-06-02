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
    Csurname VARCHAR (45),
    Expenses FLOAT,
    Gender VARCHAR(6),
    Nationality VARCHAR(40)
) ENGINE=InnoDB""")

db1.create_table(TABLES['client'])

cols = ("Cname", "Csurname", "Expenses", "Gender", "Nationality")

with open ("src/controller/client_data.csv", 'r') as data:
    for row in data:
        db1.insert_row("client", cols, str(data))

 
#db1.cnx.commit()

print ("Sucess!")

