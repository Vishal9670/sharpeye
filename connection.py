
import pyodbc
class db_connection :
    def get_db_connection():
        connection_string = (
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-MVGO5U1\\SQLEXPRESS;'
        'DATABASE=vishaldb;'
        'UID=vishal;'
        'PWD=Vishal;' 
        "Trusted_Connection=yes" 
        )
        conx=pyodbc.connect(connection_string)
        return conx    
       

    
   




