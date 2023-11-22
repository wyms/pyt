import os
import pandas as pd
import yfinance as yf  # Corrected import statement

S_AND_P_URL = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'

def get_ticker_data(tickers: list):
    data = yf.download(
        tickers=tickers,
        interval='1d',
        group_by='ticker',
        threads=True  # Added a comma at the end of the previous line
    )

    data = data.T
    all_downloaded_tickers = list(set([id[0] for id in data.index]))

    for ticker in all_downloaded_tickers:
        df = data.loc[ticker, :].T.sort_index().dropna()
        df.to_csv(f'data/{ticker}.csv', index=True)

# Corrected function name
def get_s_and_p_tickers() -> list:
    return pd.read_html(S_AND_P_URL)[0]['Symbol'].tolist()

if __name__ == '__main__':
    # Check if a directory exists called 'data', if not, create it
    if not os.path.isdir('data'):
        os.mkdir('data')

    # Download one csv file per ticker and place it in the data directory
    get_ticker_data(get_s_and_p_tickers())




