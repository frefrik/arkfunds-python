import requests
import pandas as pd
from io import StringIO
from urllib.parse import urlencode
from datetime import datetime, timedelta
from .utils import get_useragent


class YahooFinance:
    quote_url = "https://query2.finance.yahoo.com/v7/finance/options/{0}"
    history_url = "https://query1.finance.yahoo.com/v7/finance/download/{0}"

    def __init__(self, symbol):
        self.symbol = symbol
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": get_useragent(__class__.__name__)})

    def _get(self, url, params=None):
        res = self.session.get(url, params=params, timeout=self.timeout)
        res.raise_for_status()

        return res

    def _update_quote(self):
        res = self._get(self.quote_url.format(self.symbol))

        if res.status_code == 404:
            raise LookupError("Symbol not found.")
        else:
            res.raise_for_status()

        _json = res.json()["optionChain"]["result"][0]["quote"]

        self.yf_ticker = _json.get("symbol")
        self.yf_price = _json.get("regularMarketPrice")
        self.yf_currency = _json.get("currency")
        self.yf_exchange = _json.get("exchange")
        self.yf_change = _json.get("regularMarketChange")
        self.yf_changep = _json.get("regularMarketChangePercent")
        self.yf_last_trade = datetime.utcfromtimestamp(_json.get("regularMarketTime"))
        self.yf_name = _json.get("longName", "")

    def price_history(self, days_back, frequency):
        dt = timedelta(days=days_back)
        frequency = {"m": "mo", "w": "wk", "d": "d"}[frequency]

        now = datetime.utcnow()
        dateto = int(now.timestamp())
        datefrom = int((now - dt).timestamp())

        url = self.history_url.format(self.symbol)
        params = {
            "period1": datefrom,
            "period2": dateto,
            "interval": f"1{frequency}",
            "events": "history",
        }
        param_string = urlencode(params).replace("%5Cu002F", "/")

        res = self._get(url, params=param_string)
        res.raise_for_status()
        return pd.read_csv(StringIO(res.text), parse_dates=["Date"])

    @property
    def price(self):
        self._update_quote()
        return self.yf_price

    @property
    def last_trade(self):
        self._update_quote()
        return self.yf_last_trade

    @property
    def change(self):
        self._update_quote()
        return self.yf_change

    @property
    def changep(self):
        self._update_quote()
        return self.yf_changep
