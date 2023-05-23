import inspect
import os
import sys

current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from model.db_model import bdd

db1 = bdd()

db1.select_db("eshop")

print ("Sucess!")



