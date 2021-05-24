import pandas as pd
import numpy as np
import os
# use get_db_url function to connect to the codeup db
from env import get_db_url

def get_telco_data(cached=False):
    '''
    This function returns the telco churn database as a pandas dataframe. If the data is cached or the file exists in the directory, the
    function will read the data into a df and return it. Otherwise, the function will read the database into a dataframe, cache it as a csv file
    and return the dataframe.
    '''
    # If the cached parameter is false, or the csv file is not on disk, read from the database into a dataframe
    if cached == False or os.path.isfile('telco_df.csv') == False:
        sql_query = '''
        SELECT * 
        FROM customers 
        JOIN contract_types USING (contract_type_id)
        JOIN internet_service_types USING (internet_service_type_id)
        JOIN payment_tyoes USING (payment_type_id);
        '''
        telco_df = pd.read_sql(sql_query, get_db_url('telco_churn'))
         #also cache the data we read from the db, to a file on disk
        telco_df.to_csv('telco_df.csv')
    else:
        # either the cached parameter was true, or a file exists on disk. Read that into a df instead of going to the database
        telco_df = pd.read_csv('telco_df.csv', index_col=0)
    # return our dataframe regardless of its origin
    return telco_df

