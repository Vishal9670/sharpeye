
import pandas as pd
from connection import get_db_connection


connection = get_db_connection()

if connection:
    query = "SELECT * FROM cdc"
    df = pd.read_sql(query, connection)
    print(df)
    
    connection.close()
else:
    print("Failed to connect to the database.")
