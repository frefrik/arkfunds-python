from datetime import date

import pandas as pd

from .arkfunds import ArkFunds
from .utils import _convert_to_list
from .yahoo import YahooFinance


class Stock(ArkFunds):
    """Class for accessing Stock data"""

    _COLUMNS = {
        "profile": [
            "ticker",
            "name",
            "country",
            "industry",
            "sector",
            "fullTimeEmployees",
            "summary",
            "website",
            "market",
            "exchange",
            "currency",
            "marketCap",
            "sharesOutstanding",
        ],
        "ownership": [
            "ticker",
            "date",
            "fund",
            "weight",
            "weight_rank",
            "shares",
            "market_value",
        ],
        "trades": [
            "date",
            "fund",
            "direction",
            "ticker",
            "company",
            "cusip",
            "shares",
            "etf_percent",
        ],
    }

    def __init__(self, symbols: str):
        """Initialize

        Args:
            symbol (str): Stock ticker
        """
        super(Stock, self).__init__(symbols)
        self.symbols = _convert_to_list(symbols)

        try:
            self.yf = YahooFinance(self.symbols)
        except Exception:
            self.yf = None

    def _dataframe(self, symbols, params):
        endpoint = params["endpoint"]
        columns = self._COLUMNS[endpoint]
        dataframes = []

        for symbol in symbols:
            params["query"]["symbol"] = symbol
            data = self._get(params)

            if data:
                if endpoint == "profile":
                    df = pd.DataFrame(data, columns=columns, index=[0])
                else:
                    df = pd.DataFrame(data[endpoint], columns=columns)

                if endpoint == "ownership":
                    df["ticker"] = data.get("symbol")
                    df["date"] = data.get("date")

                dataframes.append(df)

        if not dataframes:
            return f"Stock.{endpoint}: No data found for {symbols}"
        else:
            return pd.concat(dataframes, axis=0).reset_index(drop=True)

    def profile(self):
        """Get Stock profile information

        Returns:
            dict
        """
        params = {
            "key": "stock",
            "endpoint": "profile",
            "query": {},
        }

        return self._dataframe(self.symbols, params)

    def fund_ownership(self):
        """Get Stock Fund Ownership

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "stock",
            "endpoint": "ownership",
            "query": {},
        }

        return self._dataframe(self.symbols, params)

    def trades(
        self, direction: str = None, date_from: date = None, date_to: date = None
    ):
        """Get Stock Trades

        Args:
            direction (str, optional): 'Buy' or 'Sell'. Defaults to None.
            date_from (date, optional): From-date in ISO 8601 format.. Defaults to None.
            date_to (date, optional): To-date in ISO 8601 format.. Defaults to None.

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "stock",
            "endpoint": "trades",
            "query": {
                "direction": [direction.lower() if direction else None],
                "date_from": date_from,
                "date_to": date_to,
            },
        }

        return self._dataframe(self.symbols, params)

    def price(self):
        """Get current stock price info

        Returns:
            pandas.DataFrame
        """
        if self.yf:
            return self.yf.price

    def price_history(self, days_back=7, frequency="d"):
        """Get historical price data for ticker

        Args:
            days_back (int, optional): Number of days with history. Defaults to 7.
            frequency (str, optional): Valid params: 'd' (daily), 'w' (weekly), 'm' (monthly). Defaults to "d".

        Returns:
            pandas.DataFrame
        """
        if self.yf:
            return self.yf.price_history(days_back=days_back, frequency=frequency)
