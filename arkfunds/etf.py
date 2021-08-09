from datetime import date

import pandas as pd

from .arkfunds import ArkFunds
from .utils import _convert_to_list


class ETF(ArkFunds):
    """Class for accessing ARK ETF data"""

    def __init__(self, symbols: str):
        """Initialize

        Args:
            symbols (str or list): ARK ETF symbol or list collection of symbols
        """
        super(ETF, self).__init__(symbols)
        self.symbols = _convert_to_list(symbols)
        self._validate_symbols()

    def _validate_symbols(self):
        valid_symbols = []
        invalid_symbols = []

        for symbol in self.symbols:
            if symbol in self.ARK_FUNDS:
                valid_symbols.append(symbol)
            else:
                invalid_symbols.append(symbol)

        self.symbols = valid_symbols
        self.invalid_symbols = invalid_symbols or None

        if self.invalid_symbols:
            raise ValueError(
                f"Invalid symbols: {self.invalid_symbols}. Only ARK ETF symbols accepted: {', '.join(self.ARK_FUNDS)}"
            )

    def _dataframe(self, symbols, params):
        endpoint = params["endpoint"]
        dataframes = []

        for symbol in symbols:
            params["query"]["symbol"] = symbol
            data = self._get(params)

            df = pd.DataFrame(data[endpoint])

            if endpoint == "holdings":
                _date = data.get("date")
                df.insert(0, "fund", symbol)
                df.insert(1, "date", _date)

            if endpoint == "trades":
                df.insert(0, "fund", symbol)

            dataframes.append(df)

        df = pd.concat(dataframes, axis=0).reset_index(drop=True)

        return df

    def profile(self):
        """Get ARK ETF profile information

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "etf",
            "endpoint": "profile",
            "query": {},
        }

        return self._dataframe(self.symbols, params)

    def holdings(self, _date: date = None):
        """Get ARK ETF holdings

        Args:
            date (date, optional): Fund holding date in ISO 8601 format. Defaults to None.

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "etf",
            "endpoint": "holdings",
            "query": {
                "date": _date,
            },
        }

        return self._dataframe(self.symbols, params)

    def trades(self, period: str = "1d"):
        """Get ARK ETF intraday trades

        Args:
            period (str, optional): Valid periods: 1d, 7d, 1m, 3m, 1y, ytd. Defaults to "1d".

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "etf",
            "endpoint": "trades",
            "query": {
                "period": period,
            },
        }

        return self._dataframe(self.symbols, params)

    def news(self, date_from: date = None, date_to: date = None):
        """Get ARK ETF news

        Args:
            date_from (date, optional): From-date in ISO 8601 format. Defaults to None.
            date_to (date, optional): To-date in ISO 8601 format. Defaults to None.

        Returns:
            pandas.DataFrame
        """
        params = {
            "key": "etf",
            "endpoint": "news",
            "query": {
                "date_from": date_from,
                "date_to": date_to,
            },
        }

        return self._dataframe(self.symbols, params)
