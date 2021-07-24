from datetime import date
from .arkfunds import ArkFunds


class Stock(ArkFunds):
    """Class for accessing Stock data"""

    def __init__(self, symbol: str):
        """Initialize

        Args:
            symbol (str): Stock ticker
        """
        super().__init__()
        self.symbol = symbol

    def profile(self, df: bool = False):
        """Get Stock profile information

        Args:
            df (bool, optional): Return pandas.DataFrame. Defaults to False.

        Returns:
            dict
        """
        params = {
            "symbol": self.symbol,
        }

        res = self._get(key="stock", endpoint="profile", params=params)
        _json = res.json()

        return self._data(_json, df)

    def fund_ownership(self, df: bool = True):
        """Get Stock Fund Ownership

        Args:
            df (bool, optional): Return pandas.DataFrame. Defaults to True.

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
        }

        res = self._get(key="stock", endpoint="fund-ownership", params=params)
        _json = res.json()["ownership"]

        return self._data(_json, df)

    def trades(
        self,
        direction: str = None,
        date_from: date = None,
        date_to: date = None,
        df: bool = True,
    ):
        """Get Stock Trades

        Args:
            direction (str, optional): 'Buy' or 'Sell'. Defaults to None.
            date_from (date, optional): From-date in ISO 8601 format.. Defaults to None.
            date_to (date, optional): To-date in ISO 8601 format.. Defaults to None.
            df (bool, optional): Return pandas.DataFrame. Defaults to True.

        Returns:
            pandas.DataFrame
        """
        params = {
            "symbol": self.symbol,
            "direction": [direction.lower() if direction else None],
            "date_from": date_from,
            "date_to": date_to,
        }

        res = self._get(key="stock", endpoint="trades", params=params)
        _json = res.json()["trades"]

        return self._data(_json, df)
