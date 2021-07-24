import requests
import pandas as pd
from .utils import get_useragent


class ArkFunds:
    BASE_URL = "https://arkfunds.io/api/v1"
    ENDPOINTS = {
        "etf": {
            "profile": "/etf/profile",
            "holdings": "/etf/holdings",
            "trades": "/etf/trades",
            "news": "/etf/news",
        },
        "stock": {
            "profile": "/stock/profile",
            "ownership": "/stock/fund-ownership",
            "trades": "/stock/trades",
        },
    }

    def __init__(self):
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": get_useragent(__class__.__name__)})

    def _get(self, key, endpoint, params):
        res = self.session.get(
            self.BASE_URL + self.ENDPOINTS[key][endpoint],
            params=params,
            timeout=self.timeout,
        )
        res.raise_for_status()

        return res

    def _dataframe(self, _json, key=None, endpoint=None):
        data = _json[endpoint]
        df = pd.DataFrame(data)

        if key == "etf":
            if endpoint == "holdings":
                symbol = _json.get("symbol")
                _date = _json.get("date")
                df.insert(0, "date", _date)
                df.insert(1, "fund", symbol)

            if endpoint == "trades":
                symbol = _json.get("symbol")
                df.insert(1, "fund", symbol)

        if key == "stock" and endpoint == "ownership":
            symbol = _json.get("symbol")
            _date = _json.get("date")
            df.insert(0, "date", _date)
            df.insert(1, "ticker", symbol)

        return df
