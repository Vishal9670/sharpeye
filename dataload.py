import pandas as pd


class data_load :
    def load(self,query ,conx):
        df_data= pd.read_sql(query,conx)
        return df_data
    
    def load_execute(self,query,conx):
        
        df_data=conx.execute(query)
        