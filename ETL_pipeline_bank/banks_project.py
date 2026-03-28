# Importing the required libraries
import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

# variable
url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ['Name', 'MC_USD_Billion']
rate_csv = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv'
output_csv = './Largest_banks_data.csv'
dbname = 'Banks.db'
table_name = 'Largest_banks'
log_file = 'code_log.txt'

def log_progress(message):
    timestamp = '%Y-%m-%d-%H:%M:%S'
    now = datetime.now()
    timestamp = now.strftime(timestamp)
    with open ('./code_log.txt','a') as f:
        f.write(timestamp + " : " + message + '\n')

def extract(url, table_attribs):
    raw_list = []
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    container = data.find('div', class_='mw-parser-output')
    tbody = container.find('table').find('tbody')
    rows = tbody.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        if len(cols) >= 3:
            market_cap = float(cols[2].get_text(strip=True))
            links = cols[1].find_all('a')
            dict_a = {'Name': links[1].get_text(),'MC_USD_Billion': market_cap}
            raw_list.append(dict_a)
    df = pd.DataFrame(raw_list,columns = table_attribs)
    return df

def transform(df, csv_path):
    df_rate = pd.read_csv(csv_path)
    dict_rate = df_rate.set_index('Currency').to_dict()['Rate']
    gbp_rate = float(dict_rate['GBP'])
    eur_rate = float(dict_rate['EUR'])
    inr_rate = float(dict_rate['INR'])
    gbp_list = []
    eur_list = []
    inr_list = []   
    for x in df['MC_USD_Billion'] :
        gbp_list.append(np.round(x * gbp_rate, 2))
        eur_list.append(np.round(x * eur_rate, 2))
        inr_list.append(np.round(x * inr_rate, 2))
    df['MC_GBP_Billion'] = gbp_list
    df['MC_EUR_Billion'] = eur_list
    df['MC_INR_Billion'] = inr_list 

    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path, index=False)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name,sql_connection, if_exists = 'replace', index = False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)

# Main
log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)
log_progress('Data extraction complete. Initiating Transformation process')

df = transform(df, rate_csv)
log_progress('Data transformation complete. Initiating Loading process')

load_to_csv(df, output_csv)
log_progress('Data saved to CSV file')

sql_connection = sqlite3.connect(dbname)
log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)
log_progress('Data loaded to Database as table. Executing  the query')

query1 = 'SELECT * FROM Largest_banks'
query2 = 'SELECT AVG(MC_GBP_Billion) FROM Largest_banks'
query3 = 'SELECT Name from Largest_banks LIMIT 5'
run_query(query1, sql_connection)
run_query(query2, sql_connection)
run_query(query3, sql_connection)
log_progress('Process Complete.')

sql_connection.close()
log_progress('Server Connection closed.')
