
import pyodbc
class db_connection :
    def get_db_connection(self):
        connection_string = (
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-MVGO5U1\\SQLEXPRESS;'
        'DATABASE=vishaldb;'
        'UID=vishal;'
        'PWD=Vishal;' 
        "Trusted_Connection=yes" 
    

        )
        
        return connection_string       
    

    
   




