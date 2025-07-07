import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
tables = soup.find_all("table")
for table in tables:
    if "GameStop Quarterly Revenue" in str(table):
        gme_table = table
        break
gme_revenue = pd.read_html(str(gme_table))[0]
gme_revenue.dropna(inplace=True)
print(gme_revenue.tail())
