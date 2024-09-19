from function_Call import store_procedure
from dataload import data_load
from connection import db_connection

conx= db_connection.get_db_connection()
data_loader= data_load()
store_procedure = store_procedure()
class data_m_store:

    def __init__(self):
        self.time_date= {}

    def data_manipulation(self):
        
        df_data_emp= store_procedure.emp_data()
        print("df_data_emp")
        df_data_sales= store_procedure.sales_data()
        df_data_performance = store_procedure.performance_data()
        #time taken from cdc tables 
      
        df_data_emp_time= df_data_emp['prev_time_stamp']
        df_data_sales_time=df_data_sales['prev_time_stamp']
        df_data_performance= df_data_performance['prev_time_stamp']
        #all table prev time store in dictionary
        self.time_date['emp_time_cdc']=df_data_emp_time.item()  
        self.time_date['sales_time_cdc']= df_data_sales_time.item()
        self.time_date['performance_time_cdc']= df_data_performance.item()       
        
    def emp_fetch_data(self):
        
        emp_time_cdc = self.time_date.get('emp_time_cdc')
        sql_query= f"EXEC usp_get_emp '{emp_time_cdc}'"
        if conx:
            df_emp_table_data = data_loader.load(sql_query,conx)
            print(df_emp_table_data)
            return None
        else:
            print("problem with connection ") 
    def sales_fetch_data(self):
        sales_time_cdc = self.time_date.get('sales_time_cdc')
        sql_query=  f"EXEC usp_get_sales '{sales_time_cdc}'"   
        if conx:
            df_sales_table_data = data_loader.load(sql_query,conx)
           # print(df_sales_table_data)
            return None
        else:
            print("problem with connection ") 
    def performance_fetch_data(self):
        performance_time_cdc = self.time_date.get('performance_time_cdc')
        sql_query= f"EXEC usp_get_perfromance '{performance_time_cdc}'"       
        if conx:
            df_performance_table_data = data_loader.load(sql_query,conx)
            #print(df_performance_table_data)
            return None
        else:
            print("problem with connection ")  
