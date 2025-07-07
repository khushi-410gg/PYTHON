import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
soup = BeautifulSoup(html_data, "html.parser")
tables = soup.find_all("table")
for table in tables:
    if "Tesla Quarterly Revenue" in str(table):
        tesla_table = table
        break
tesla_revenue = pd.read_html(str(tesla_table))[0]
tesla_revenue.dropna(inplace=True)
print(tesla_revenue.tail())


