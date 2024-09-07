import pyodbc
import pandas as pd

connection_string = (
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-MVGO5U1\\SQLEXPRESS;'
        'DATABASE=vishaldb;'
        'UID=vishal;'
        'PWD=Vishal;' 
        "Trusted_Connection=yes" 
    ) 
conx=pyodbc.connect(connection_string)
sql_query= ("EXEC usp_get_data_sales")
df_data_sales=pd.read_sql(sql_query,conx)
print(df_data_sales)
conx.close()
