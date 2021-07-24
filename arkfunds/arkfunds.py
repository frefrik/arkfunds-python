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
            "fund-ownership": "/stock/fund-ownership",
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

    def _data(self, data, ret_df):
        if ret_df:
            try:
                df = pd.DataFrame(data)
            except ValueError:
                df = pd.DataFrame(data, index=[0])
            return df
        else:
            return data
