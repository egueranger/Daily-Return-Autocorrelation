from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

#===============================================================================
# Tiingo API and data recovery (AI generated)

import requests
import pandas as pd
from datetime import datetime

class TiingoClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.tiingo.com/tiingo"

    def get_close_prices(self, ticker: str, start_date: str, end_date: str):
        """
        Given a ticker, recovers adjusted daily prices.
        start_date et end_date 'YYYY-MM-DD' form.
        """
        url = f"{self.base_url}/daily/{ticker}/prices"
        params = {
            "token": self.api_key,
            "startDate": start_date,
            "endDate": end_date,
            "format": "json"
        }

        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        # Convert to DataFrame
        df = pd.DataFrame(data)
        df["date"] = pd.to_datetime(df["date"])
        df.set_index("date", inplace=True)

        return df["adjClose"].tolist()

API_KEY = "eddfccbe3cca986363149ab559b5e62d91fcbfd4"
client = TiingoClient(API_KEY)

#===============================================================================
# My own algorithm
#===============================================================================

# Compute daily log returns

index = ["AAPL", "NVDA", "V", "SPGI", "WMT", "DIS", "PM", "XOM", "O"]
corrs = []
n_days = []

for stock in index:
    prices = np.array(client.get_close_prices(stock, "2000-01-01", "2026-03-25"))
    n = len(prices)-1
    returns = np.log(prices[1:]/prices[:-1])
    corr = np.corrcoef(returns[:-1], returns[1:])[0, 1]
    # p-value
    p = 2*norm.cdf(-np.sqrt(n)*abs(corr))
    print(stock, corr, p, n)
    corrs.append(corr)
    n_days.append(n)

#corrs = np.array([-0.03624716776010853, -0.007561370410012947, -0.10431786244175983, -0.03549838848907282, -0.03388027252863604, -0.041918843321657795, -0.04881136117503521, -0.06888733684278146, -0.1296450676669594])

#n_days = [6595, 6595,4532, 6337, 6595, 6595, 4534, 6595, 6595]

errors = [1.96/np.sqrt(n) for n in n_days]

plt.bar(index, corrs, color="grey", edgecolor='black', alpha=0.8)

thresholds = 1.96/np.sqrt(n_days)

plt.errorbar(index, [0]*len(index), yerr=thresholds, color='black', capsize=5)

errors = [1.96/np.sqrt(n) for n in n_days]

plt.ylabel("Day/Day+1 correlation")
plt.title("Empirical daily autocorrelation")

plt.show()