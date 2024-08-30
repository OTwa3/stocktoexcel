import os
import requests
import pandas as pd
import openpyxl





ticker = "TSLA"
date = "2023-01-09"


# Define your API key and endpoint
api_key = "FTxQsPJCQxnUHICKYZxGuaLF1OIpWALc"
#url = f"https://api.polygon.io/v3/reference/tickers?ticker={ticker}&active=true&limit=100&apiKey={api_key}"
url = f"https://api.polygon.io/v1/open-close/{ticker}/{date}?adjusted=true&apiKey={api_key}"


combined_df = pd.DataFrame()

# Step 1: Get data from the API
response = requests.get(url)
data = response.json()

# Step 2: Process the JSON data
# Assuming that the data is in the 'results' key
#tickers = data.get('results', [])

# Step 3: Convert the data to a DataFrame
df = pd.DataFrame([data])

# Select relevant columns (adjust as needed)
#df = df[['ticker', 'name', 'market', 'locale', 'currency_name']]
df = df[['symbol', 'open', 'close', 'high', 'low', 'volume']]



# Step 4: Write the DataFrame to an Excel file
excel_filepath = r'C:\Users\owent\OneDrive\Documents\ExcelFiles\Test.xlsx'


# Check if the file exists
if os.path.exists(excel_filepath):
    # If it exists, load the existing data
    print("File exists, appending data...")
    existing_df = pd.read_excel(excel_filepath)
    
    # Append the new data to the existing data
    combined_df = pd.concat([existing_df, df], ignore_index=True)
    print(combined_df.head())
    combined_df.to_excel(excel_filepath, index=False)
else:
    # If it doesn't exist, write the new data to a new file
    print("File does not exist, writing data...")
    df.to_excel(excel_filepath, index=False)


print(f"Data has been written to {excel_filepath}")
