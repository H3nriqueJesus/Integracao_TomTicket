import mysql.connector
from mysql.connector import errorcode

def connect_tomticket_prod():
    try:
        cnx = mysql.connector.connect(user='user', password='Ledax!@#',
                              host='192.168.0.230',
                              database='TOMTICKET')
        db_info = cnx.get_server_info()
        print("Conectado ao MySql versao " + str(db_info))
        return cnx
    except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
      elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
      else:
        print(err)
    else:
     
     cnx.close()
