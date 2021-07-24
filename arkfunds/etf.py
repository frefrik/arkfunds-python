from datetime import date
from .arkfunds import ArkFunds
from .yahoo import YahooFinance


class ETF(ArkFunds):
    """Class for accessing ARK ETF data"""

    def __init__(self, symbol: str):
        """Initialize

        Args:
            symbol (str): ARK ETF symbol
        """
        super().__init__()
        self.symbol = symbol

        try:
            self.yf = YahooFinance(self.symbol)
        except Exception:
            self.yf = None

    def profile(self):
        """Get ARK ETF profile information

        Returns:
            dict
        """
        params = {
            "symbol": self.symbol,
        }

        res = self._get(key="etf", endpoint="profile", params=params)

        return res.json()["profile"]

    def holdings(self, date: date = None):
        """Get ARK ETF holdings

        Args:
            date (date, optional): Fund holding date in ISO 8601 format. Defaults to None.

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
            "date": date,
        }

        res = self._get(key="etf", endpoint="holdings", params=params).json()

        return self._dataframe(res, key="etf", endpoint="holdings")

    def trades(self, period: str = "1d"):
        """Get ARK ETF intraday trades

        Args:
            period (str, optional): Valid periods: 1d, 7d, 1m, 3m, 1y, ytd. Defaults to "1d".

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
            "period": period,
        }

        res = self._get(key="etf", endpoint="trades", params=params).json()

        return self._dataframe(res, key="etf", endpoint="trades")

    def news(self, date_from: date = None, date_to: date = None):
        """Get ARK ETF news

        Args:
            date_from (date, optional): From-date in ISO 8601 format. Defaults to None.
            date_to (date, optional): To-date in ISO 8601 format. Defaults to None.

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
            "date_from": date_from,
            "date_to": date_to,
        }

        res = self._get(key="etf", endpoint="news", params=params).json()

        return self._dataframe(res, key="etf", endpoint="news")

    def price(self):
        """Get current ticker price

        Returns:
            float
        """
        if self.yf:
            return self.yf.price

    def last_trade(self):
        """Get last trade date

        Returns:
            datetime.datetime
        """
        if self.yf:
            return self.yf.last_trade

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

    def price_history(self, days_back=7, frequency="d"):
        """Get historical price data for ticker

        Args:
            days_back (int, optional): Number of days with history. Defaults to 7.
            frequency (str, optional): Valid params: 'd' (daily), 'w' (weekly), 'm' (monthly). Defaults to "d".

        Returns:
            pandas.DataFrame
        """
        if self.yf:
            return self.yf.get_history(days_back=days_back, frequency=frequency)
