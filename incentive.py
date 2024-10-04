from connection import db_connection
from connection1 import connection_1
import pandas as pd
from dataload import data_load
connection_1=connection_1()
conn=connection_1.connection_2()
data_loder=data_load()
conx= db_connection.get_db_connection()
conx.autocommit=True
class basic_data:
    def __init__(self):
        self.df_emp=pd.DataFrame()
        self.df_sales=pd.DataFrame()
        self.df_performanc=pd.DataFrame()
        self.df_finall_data=pd.DataFrame()

    def emp_basic(self):
        query= "SELECT * FROM employee"
        df_emp1=data_loder.load(query,conx)
        self.df_emp=df_emp1

    
    def sales_basic(self):
        query= "SELECT * FROM sales"
        df_sales1=data_loder.load(query,conx)
        self.df_sales=df_sales1

    def performance_basic(self):
        query= "SELECT * FROM performance"
        df_performace1=data_loder.load(query,conx) 
        self.df_performanc=df_performace1
       
        #self.data['performance_data']=df_performace

    def merge_all_tables(self):
        emp= self.df_emp
        performance=self.df_performanc
        sales=self.df_sales
        #df_finall=pd.concat([sales,emp,performance],ignore_index=True)
        df_finall=sales.merge(emp,on='eid',how='inner').merge(performance,on='eid',how='inner')      
        #df_finall.info()   
        self.df_finall_data=df_finall
        #df_finall.describe()
        #df_finall.head()
        #print(df_finall)
        #df_finall.to_sql('stage_incentive',conx,index=False , if_exists='append')
        df_finall.to_sql('stage_incentive',con=conn,index=False , if_exists='replace')
        print("df finall is ok")
        

    def update_stag_incentive(self):    
        query="EXEC usp_merge_incentive"
        stage_incentive=data_loder.load_execute(query,conx)
    def update_incentive(self):
        query=("EXEC final_incentive")
        update_incentive=data_loder.load_execute(query,conx)
        print("finally incentive calculated ")

''' 
obj=basic_data()
obj.emp_basic()
obj.sales_basic()
obj.performance_basic()
obj.merge_all_tables()
obj.update_stag_incentive()
obj.update_incentive()
'''