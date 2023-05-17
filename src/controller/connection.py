import mysql.connector
from mysql.connector import errorcode
from ..model.credential import credentials


creds = credentials()

try:
    cnx = mysql.connector.connect(user=creds.user, password=creds.password, host=creds.host, database=creds.database)
    
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
    
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
    
  else:
    print(err)