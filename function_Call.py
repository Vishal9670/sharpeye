from dataload import data_load
import pyodbc
from connection import db_connection

db_connections = db_connection()

#data=db_connections.test()
conx= db_connection.get_db_connection()
#create instance of object 
data_loader= data_load()
#create for emp data frame 
class store_procedure :
    def emp_data(self):
        sql_query = "EXEC usp_get_cdc_data employee"
        if conx :
            df_data_emp = data_loader.load(sql_query,conx)
            print("df_data_emp")
            return df_data_emp
        else:
            print("problem with connection ")
    def sales_data(self):
        sql_query= "EXEC usp_get_cdc_data sales"
        if conx :
           df_data_sales = data_loader.load(sql_query,conx)
           return df_data_sales
        else:
           print("problem with connection ")
# for df performance
    def performance_data(self):
        sql_query= "EXEC usp_get_cdc_data performance"
        if conx :
          df_data_performance = data_loader.load(sql_query,conx)
          return df_data_performance
        else:
           print("problem with connection ")


#conx.close()           
