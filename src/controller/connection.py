import mysql.connector
from model.credential import credentials


creds = credentials()

cnx = mysql.connector.connect(user=creds.user, password=creds.password, host=creds.host, database=creds.database)