import pandas as pd
import  numpy as np
import requests
import sqlite3
from datetime import datetime
from bs4 import BeautifulSoup

url= 'https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks'

table_attribs_ue=['Name', 'MC_USD_Billion']

db_name='Banks.db'

table_name='Largest_banks'

out_path='./Largest_banks_data.csv'

csv_path= 'exchange_rate.csv'

#table_attribs_fi=['Name', 'MC_USD_millions', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']

page=requests.get(url).text
soup=BeautifulSoup(page, "html.parser")


def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''
    
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

def extract(url, table_attribs_ue):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''
    
    
    df=pd.DataFrame(columns=table_attribs_ue)
    tables=soup.find_all('tbody')
    rows=tables[0].find_all('tr')
    L=[]
    
    for row in rows[1:]:
        L.append(row.find_all('td'))
        for i in range(len(L)):   
            data_dict={'Name': L[i][1].find_all('a')[1].contents[0],  "MC_USD_Billion": np.float64(L[i][2].contents[0].strip())}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df,df1], ignore_index=True)
            L=list()
    return df

def transform(df, csv_path):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''
    
    dataframe=pd.read_csv(csv_path)
    
    exchangedict = dataframe.set_index('Currency').to_dict()['Rate']
    
    df['MC_GBP_Billion'] = [np.round(x*exchangedict['GBP'],2) for x in df['MC_USD_Billion']]
    df['MC_EUR_Billion'] = [np.round(x*exchangedict['EUR'],2) for x in df['MC_USD_Billion']]
    df['MC_INR_Billion'] = [np.round(x*exchangedict['INR'],2) for x in df['MC_USD_Billion']]
      
    return df

def load_to_csv(df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''
    
    df.to_csv(out_path)

def load_to_db(df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''
    
    df.to_sql(table_name, sql_connection, if_exists='replace')

def run_query(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''
    
    for query in query_statement:
        print(query)
        query_output = pd.read_sql(query, sql_connection)
        print(query_output)

''' Here, you define the required entities and call the relevant
functions in the correct order to complete the project. Note that this
portion is not inside any function.'''

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs_ue)

log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, csv_path)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, out_path)

log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect('World_Economies.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

query_statement =["SELECT * FROM Largest_banks", "SELECT AVG(MC_GBP_Billion) FROM Largest_banks", "SELECT Name from Largest_banks LIMIT 5" ]
run_query(query_statement, sql_connection)

log_progress('Process Complete.')

sql_connection.close()
