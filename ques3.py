import yfinance as yf
gme_data = yf.download('GME', period='30d')
gme_data.reset_index(inplace=True)
print(gme_data.head())
