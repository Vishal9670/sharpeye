import urllib

import sqlalchemy as sal
import pandas as pd
class connection_1:
    def connection_2(self):
        server ='DESKTOP-MVGO5U1\\SQLEXPRESS'
        mydatabase='vishaldb'
        myuserid='vishal'
        mypassword='Vishal'
        driver='SQL Server' 
        params = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};"
                                         "SERVER=DESKTOP-MVGO5U1\\SQLEXPRESS;"
                                        "DATABASE=vishaldb;"
                                        "UID=vishal;"
                                        "PWD=Vishal;"
                                        "Trusted_Connection=yes")
                                 
        engine= sal.create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        conn=engine.connect()
        return conn

'''  
if conn:
    print("connection is ok")
else:
    print("something wrong ")    
import pandas as pd

# Create a dictionary with the data
data = {
    'eid': [1, 2, 3],
    'sales': [345, 300, 400],
    'modify_by': ['vishal', 'vishal', 'ashwani'],
    'created_by': ['1990-01-01', '1990-01-01', '2023-01-01'],
    'modify_date': ['1990-01-04', '1990-01-04', '2023-01-04'],
    'created_date': ['abhi', 'abhi', 'vishal']
}
df = pd.DataFrame(data)



df.to_sql('sales',con=conn,index=False , if_exists='replace')

'''