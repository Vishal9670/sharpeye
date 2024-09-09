import pyodbc
import pandas as pd
from dataload import data_load
from connection import db_connection
from function_Call import store_procedure
from data_store import data_m_store
from update_cdc import update_date_today

data_m = data_m_store()


data_m.data_manipulation()
data_m.emp_fetch_data()
data_m.sales_fetch_data()
data_m.performance_fetch_data()


obj=update_date_today()
obj.cdc_today_update_sales()        
obj.cdc_today_update_emp()
obj.cdc_today_update_performance()







 
