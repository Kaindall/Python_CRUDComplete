import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from model.db_model import bdd

db1 = bdd()

DB_NAME = "eshop"

db1.delete_db(DB_NAME)

db1.select_db(DB_NAME, force=True)

TABLES = []

print ("Sucess!")




