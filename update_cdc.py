import pyodbc
from datetime import datetime
from dataload import data_load
from connection import db_connection
db_connections = db_connection()
conx = db_connection.get_db_connection()

conx.autocommit=True
data_loader= data_load()

today = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(today)
class update_date_today:
    def cdc_today_update_sales(self):
        sql_query= f"EXEC usp_update_cdc 'sales','{today}'"
        if conx:
            print("connection is ok")
            df_update= data_loader.load_execute(sql_query,conx)
        else:
            print("connectionn not established")    
            
    def cdc_today_update_emp(self):
        sql_query= f"EXEC usp_update_cdc 'employee', '{today}'"        
        if conx:
            df_update= data_loader.load_execute(sql_query,conx)
        else:
            print("connection not established")   
    def cdc_today_update_performance(self):
        sql_query = f"EXEC usp_update_cdc 'performance', '{today}'"
        if conx:
            df_update=data_loader.load_execute(sql_query,conx)
        else:
            print("connection is not established")
