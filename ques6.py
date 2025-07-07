import yfinance as yf
import matplotlib.pyplot as plt

def make_graph(data, stock, title):
    plt.figure(figsize=(10,6))
    plt.plot(data['Date'], data['Close'], label='Close Price')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Closing Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

gme_data = yf.download('GME', period='6mo')
gme_data.reset_index(inplace=True)

make_graph(gme_data, 'GME', 'GameStop Stock Price Over the Last 6 Months')
