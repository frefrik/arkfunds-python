import requests
import pandas as pd
from .utils import get_useragent


class ArkFunds:
    ARK_FUNDS = ["ARKF", "ARKG", "ARKK", "ARKQ", "ARKW", "ARKX", "IZRL", "PRNT"]
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

    def _get(self, params):
        res = self.session.get(
            self.BASE_URL + self.ENDPOINTS[params["key"]][params["endpoint"]],
            params=params["query"],
            timeout=self.timeout,
        )
        res.raise_for_status()

        return res

    def _dataframe(self, symbols, params):
        key = params["key"]
        endpoint = params["endpoint"]
        dataframes = []

        for symbol in symbols:
            params["query"]["symbol"] = symbol
            data = self._get(params).json()

            if key == "stock" and endpoint == "profile":
                df = pd.DataFrame(data, index=[0])
            else:
                df = pd.DataFrame(data[endpoint])

            if key == "etf":
                if endpoint == "holdings":
                    _date = data.get("date")
                    df.insert(0, "date", _date)
                    df.insert(1, "fund", symbol)

                if endpoint == "trades":
                    df.insert(1, "fund", symbol)

            if key == "stock" and endpoint == "ownership":
                ticker = data.get("symbol")
                _date = data.get("date")
                df.insert(0, "date", _date)
                df.insert(1, "ticker", ticker)

            dataframes.append(df)

        df = pd.concat(dataframes, axis=0).reset_index(drop=True)

        return df
