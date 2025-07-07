import yfinance as yf
tesla_data = yf.download('TSLA', period='30d')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())
