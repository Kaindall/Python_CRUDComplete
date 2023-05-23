import mysql.connector
from mysql.connector import errorcode
from .credential import credentials


creds = credentials()

class bdd:
  def __init__(self):
    self.cnx, self.act = self.connect()

  def connect(self):
    try:
      connection = mysql.connector.connect(user=creds.user, 
                                    password=creds.password, 
                                    host=creds.host, 
                                    database=creds.database)
      
      return connection, connection.cursor()
        
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        return None, print("Something is wrong with your username or password")
        
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        return None, print ("Database does not exist")
        
      else:
        return None, print(err)
  
  #create Default param to call dbChange from credentials and update config.ini
  def select_db(self, db_name, force=False):
    try:
      self.act(f"USE {db_name}")
      self.cnx.database = db_name
      
    except mysql.connector.errorcode as err:
      if (err.errno == errorcode.ER_BAD_DB_ERROR) & (force == True):
        self.create_db(db_name)
        self.cnx.database = db_name
    
    else:
      print (err)


  def create_db(self, db_name):
    try:
      self.act.execute(f"CREATE DATABASE {db_name} CHARACTER SET 'utf8'")
      
    except mysql.connector.Error as err:
      print (f"Database not created: {err}")


  def delete_db(self, db_name):
    self.act.execute(f"DROP DATABASE IF EXISTS {db_name}")

  
    