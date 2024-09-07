
import pyodbc

def get_db_connection():
    connection_string = (
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-MVGO5U1\\SQLEXPRESS;'
        'DATABASE=vishaldb;'
        'UID=vishal;'
        'PWD=Vishal;' 
        "Trusted_Connection=yes" 
    )
    
    try:
        conx = pyodbc.connect(connection_string)
        print("Connection successful")
        return conx
    except pyodbc.Error as e:
        print("Error: ", e)
        return None


