from datetime import date
from .arkfunds import ArkFunds
from .yahoo import YahooFinance


class Stock(ArkFunds):
    """Class for accessing Stock data"""

    def __init__(self, symbol: str):
        """Initialize

        Args:
            symbol (str): Stock ticker
        """
        super().__init__()
        self.symbol = symbol

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
            "symbol": self.symbol,
        }

        res = self._get(key="stock", endpoint="profile", params=params)

        return res.json()

    def fund_ownership(self):
        """Get Stock Fund Ownership

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
        }

        res = self._get(key="stock", endpoint="ownership", params=params).json()

        return self._dataframe(res, key="stock", endpoint="ownership")

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
            "symbol": self.symbol,
            "direction": [direction.lower() if direction else None],
            "date_from": date_from,
            "date_to": date_to,
        }

        res = self._get(key="stock", endpoint="trades", params=params).json()

        return self._dataframe(res, key="stock", endpoint="trades")

    def price(self):
        """Get current ticker price

        Returns:
            float
        """
        if self.yf:
            return self.yf.price

    def change(self):
        """Get current price change

        Returns:
            float
        """
        if self.yf:
            return self.yf.change

    def changep(self):
        """Get current price change in percent

        Returns:
            float
        """
        if self.yf:
            return self.yf.changep

    def last_trade(self):
        """Get last trade date

        Returns:
            datetime.datetime
        """
        if self.yf:
            return self.yf.last_trade

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
