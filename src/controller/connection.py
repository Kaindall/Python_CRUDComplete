import mysql.connector
from mysql.connector import errorcode
from .credential import credentials


creds = credentials()

class bdd:
  def __init__(self):
    self.cnx = self.connect()

  def connect(self):
    try:
      return mysql.connector.connect(user=creds.user, 
                                    password=creds.password, 
                                    host=creds.host, 
                                    database=creds.database)
        
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return None, print("Something is wrong with your user name or password")
        
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return None, print ("Database does not exist")
        
      else:
        return None, print(err)
