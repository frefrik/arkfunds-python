import requests

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

    def __init__(self, symbols):
        self.symbols = symbols
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": get_useragent(__class__.__name__)})

    def _get(self, params):
        res = self.session.get(
            self.BASE_URL + self.ENDPOINTS[params["key"]][params["endpoint"]],
            params=params["query"],
            timeout=self.timeout,
        )

        if res.status_code == 404:
            return None

        res.raise_for_status()

        return res.json()
