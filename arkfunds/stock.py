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

        res = self._get(key="stock", endpoint="fund-ownership", params=params)
        _json = res.json()["ownership"]

        return self._dataframe(_json)

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

        res = self._get(key="stock", endpoint="trades", params=params)
        _json = res.json()["trades"]

        return self._dataframe(_json)
