import pyodbc
import pandas as pd
from dataload import data_load
from connection import db_connection

db_connections = db_connection()

#data=db_connections.test()




connection_string= db_connections.get_db_connection()

conx=pyodbc.connect(connection_string)
if conx:
    print("ok connection")
else:
    print("some thing wrong in connection")


#the last line of code for test 
data_loader= data_load()
 
sql_query= "SELECT * FROM sales"
if conx :
    df_sales = data_loader.load(sql_query,conx)
    conx.close()
    print(df_sales)
else:
    print("problem woth connection ")   