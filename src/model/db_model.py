import mysql.connector
from mysql.connector import errorcode

from model.credential import credentials


creds = credentials()

class bdd:
  def __init__(self):
    self.cnx, self.act = self.connect()

  def connect(self):
    """
    Connect to MySQL with informations created with config.ini file and instantiated by credentials class.
    Returns:
        MySQLConnection: create and hold the connection to be used by cursor, like a bridge between the application and MySQL
        MySQLCursor: the cursor inside the connection class used to make every query, like a car into the bridge.
    """
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
        connection = mysql.connector.connect(user=creds.user, 
                                password=creds.password, 
                                host=creds.host)
        
        return connection, connection.cursor()

      else:
        return None, print(err)
  

  def select_db(self, db_name, force=False, default=False):
    """
    Select a database.
    Args:
      db_name: a string containing database's name to select
      force: a boolean, true indicate to create a new database if inputed value doesn't exist
      default: a boolean,true indicate to rewrite config.ini as automatic opened database with Connect
    Returns:
      A print of result and allow next queries inside the database
      """
    try:
      self.act.execute(f"USE {db_name}")
      self.cnx.database = db_name
      print (f"Database '{db_name}' selected!")
      
    except mysql.connector.Error as err:
      if (err.errno == errorcode.ER_BAD_DB_ERROR) & (force == True):
        self.create_db(db_name)
        self.cnx.database = db_name
        print ("Database doesn't exist. Created another one!")
        self.act.execute(f"USE {db_name}")
        print (f"Database '{db_name}' selected!")
    
      else:
        print (err)
    
    if default == True:
      creds.dbChange(db=db_name, default=True)
    

  def create_db(self, db_name):
    """
    Create a database.
    Args:
        db_name: generally a string containig database name to create
    """
    
    try:
      self.act.execute(f"CREATE DATABASE {db_name} CHARACTER SET 'utf8'")
      
    except mysql.connector.Error as err:
      print (f"Database not created: '{err}'")


  def delete_db(self, db_name):
    self.act.execute(f"DROP DATABASE IF EXISTS {db_name}")
    print(f"Database '{db_name}' deleted sucessfully!")

  
    