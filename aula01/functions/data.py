import pandas as pd
import yfinance as yf

def download_history(
    ticker:str,
    multi_level_index:bool = False
)-> pd.DataFrame:
    """
    download historical data from yahoo.

    Args:
        ticker (str):ticker name.
        multi_level_index (bool): Remove/include multi index.

    """
 
    df = yf.download(
        tickers= ticker,
        multi_level_index = multi_level_index
    )
    return df