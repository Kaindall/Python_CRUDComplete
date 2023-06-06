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
      default: a boolean, true indicate to rewrite config.ini with this database, turning it as a automatic connection when called Connect
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

  def create_table(self, query):
    """This method create a table inside the selected database
    Args:
      query: This can be a string, dict, tuple or list with the value of a string containing the SQL commandline to create a table
    Obs: We recommend to put in the end 'ENGINE=InnoDB'
    
    Example:
      '''
      CREATE TABLE IF NOT EXISTS Test9 (
      idClient int NOT NULL AUTO_INCREMENT,
      name varchar(45) NOT NULL,
      document int NOT NULL,
      PRIMARY KEY (idClient)
      ) ENGINE=InnoDB'''
    """
    
    if (type(query) != str) & (len(query) > 1):
      if type(query) == dict:
        for table in query.values():
          self.act.execute(table)
      
      else:
        for table in query:
          self.act.execute(table)
    
    else:
      self.act.execute(query)

  def insert_row(self, table, columns, data, recoverid=False):
    cols_lenght = ""
    for col in columns:
        if cols_lenght == "":
            cols_lenght = cols_lenght+col
        elif cols_lenght != "":
            cols_lenght = cols_lenght+f', {col}'
            
      
    if type(data) == str:
      r = data.split(sep=',')
      for e, element in enumerate(r):
          try:
              r[e] = element.replace('\n', '')
          except:
              pass
          try:
              r[e] = int(element)
          except:
              pass
      
      r = tuple(r)
        
      self.act.execute(f"""INSERT INTO {table}({cols_lenght}) VALUES{r}""")
    
      if recoverid == True:
          return self.act.lastrowid
        
    else:
      try:
        id_list = []
        for value in data:
          self.act.execute(f"""INSERT INTO {table}({cols_lenght}) VALUES{value}""")
          if recoverid == True:
            id_list.append(self.act.lastrowid)
        return id_list
      
      except:
        print ("Invalid format inputed. Please input an iterable object.")


#use an id to update a row
  def update_rowByID(self, id):
    pass
  
  def query_db(self, query):
    return self.act.execute(query)
    
    
    
    