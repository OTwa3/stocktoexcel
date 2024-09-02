import os
import sys
import requests
import pandas as pd
import openpyxl





#ticker = "TSLA"
#date = "2023-01-09"


print("Running script...")

ticker = sys.argv[1]
excel_filename = sys.argv[2]
date = sys.argv[3]


print(f"Ticker: {ticker}, Date: {date}, Excel Filename: {excel_filename}")

if not excel_filename.endswith('.xlsx'):
    excel_filename += '.xlsx'


api_key = "FTxQsPJCQxnUHICKYZxGuaLF1OIpWALc"
url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}"

print(url)

combined_df = pd.DataFrame()

response = requests.get(url)
data = response.json()

df = pd.DataFrame([data])

print(df.head())

df = df[['symbol', 'open', 'close', 'high', 'low', 'volume']]

excel_filepath = r'C:\Users\owent\OneDrive\Documents\ExcelFiles\{}'.format(excel_filename)




print(excel_filepath)

if os.path.exists(excel_filepath):
   
    print("File exists, appending data...")
    existing_df = pd.read_excel(excel_filepath)
    
    
    combined_df = pd.concat([existing_df, df], ignore_index=True)
    print(combined_df.head())
    combined_df.to_excel(excel_filepath, index=False)
else:
   
    print("File does not exist, writing data...")
    df.to_excel(excel_filepath, index=False)


print(f"Data has been written to {excel_filepath}")
