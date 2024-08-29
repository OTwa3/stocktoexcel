import requests
import pandas as pd
import openpyxl


print ("Test")


ticker = "AAPL"


# Define your API key and endpoint
api_key = "FTxQsPJCQxnUHICKYZxGuaLF1OIpWALc"
url = f"https://api.polygon.io/v3/reference/tickers?ticker={ticker}&active=true&limit=100&apiKey={api_key}"

# Step 1: Get data from the API
response = requests.get(url)
data = response.json()

# Step 2: Process the JSON data
# Assuming that the data is in the 'results' key
tickers = data.get('results', [])

# Step 3: Convert the data to a DataFrame
df = pd.DataFrame(tickers)

# Select relevant columns (adjust as needed)
df = df[['ticker', 'name', 'market', 'locale', 'currency_name']]

print("DataFrame preview:")
print(df.head())

# Step 4: Write the DataFrame to an Excel file
excel_filepath = r'C:\Users\owent\OneDrive\Documents\ExcelFiles\Test.xlsx'

df.to_excel(excel_filepath, index=False) 

print(f"Data has been written to {excel_filepath}")
