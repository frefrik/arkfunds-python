from datetime import date
from .arkfunds import ArkFunds
from .yahoo import YahooFinance
from .utils import _convert_to_list


class Stock(ArkFunds):
    """Class for accessing Stock data"""

    def __init__(self, symbol: str):
        """Initialize

        Args:
            symbol (str): Stock ticker
        """
        super().__init__()
        self.symbol = _convert_to_list(symbol)

        try:
            self.yf = YahooFinance(self.symbol)
        except Exception:
            self.yf = None

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

        return self._dataframe(self.symbol, params)

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

        return self._dataframe(self.symbol, params)

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

        return self._dataframe(self.symbol, params)

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
