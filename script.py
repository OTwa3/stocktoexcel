import os
import sys
import requests
import pandas as pd
import openpyxl
from datetime import datetime, timedelta



def get_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    return [(start + timedelta(days=x)).strftime("%Y-%m-%d") for x in range(0, (end-start).days + 1)]

print("Running script...")

ticker = sys.argv[1]
excel_filename = sys.argv[2]
startdate = sys.argv[3]
enddate = sys.argv[4]

print(f"Ticker: {ticker}, Start Date: {startdate}, End Date: {enddate}, Excel Filename: {excel_filename}")

if not excel_filename.endswith('.xlsx'):
    excel_filename += '.xlsx'

api_key = "FTxQsPJCQxnUHICKYZxGuaLF1OIpWALc"
excel_filepath = r'C:\Users\owent\OneDrive\Documents\ExcelFiles\{}'.format(excel_filename)

dates = get_dates(startdate, enddate)

combined_df = pd.DataFrame()


for date in dates:
    url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}"
    print(f"Fetching data for date: {date}")

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        df = pd.DataFrame([data])
        df = df[['symbol', 'from', 'open', 'close', 'high', 'low', 'volume']]
        
        combined_df = pd.concat([combined_df, df], ignore_index=True)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for date {date}: {e}")


print(excel_filepath)

if os.path.exists(excel_filepath):
   
    print("File exists, appending data...")
    existing_df = pd.read_excel(excel_filepath)
    
    
    combined_df = pd.concat([existing_df, combined_df], ignore_index=True)
    print(combined_df.head())
    combined_df.to_excel(excel_filepath, index=False)
else:
   
    print("File does not exist, writing data...")
    combined_df.to_excel(excel_filepath, index=False)


print(f"Data has been written to {excel_filepath}")
