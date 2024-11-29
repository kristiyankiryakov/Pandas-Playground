import yfinance as yf
import pandas as pd

data = yf.download(['SAP','TSLA'], period='1mo', group_by='ticker')

data = data.stack(level=0,future_stack=True).reset_index()

# Remove Price name 
data.columns.name = None

data.to_csv('stock_data_with_ticker.csv', index=False)

print(data.head())