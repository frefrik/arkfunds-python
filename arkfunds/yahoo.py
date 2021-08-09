from datetime import datetime, timedelta
from io import StringIO
from urllib.parse import urlencode

import pandas as pd
import requests

from .utils import get_useragent


class YahooFinance:
    quote_url = "https://query2.finance.yahoo.com/v7/finance/options/{0}"
    history_url = "https://query1.finance.yahoo.com/v7/finance/download/{0}"

    def __init__(self, symbols):
        self.symbols = symbols
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": get_useragent(__class__.__name__)})

    def _get(self, url, params=None):
        res = self.session.get(url, params=params, timeout=self.timeout)
        res.raise_for_status()

        return res

    def _update_quote(self):
        self._quote = []
        for symbol in self.symbols:
            res = self._get(self.quote_url.format(symbol))

            if res.status_code == 404:
                raise LookupError("Symbol not found.")
            else:
                res.raise_for_status()

            _json = res.json()["optionChain"]["result"][0]["quote"]

            self._quote.append(
                {
                    "ticker": _json.get("symbol"),
                    "currency": _json.get("currency"),
                    "price": _json.get("regularMarketPrice"),
                    "change": _json.get("regularMarketChange"),
                    "changep": _json.get("regularMarketChangePercent"),
                    "last_trade": datetime.utcfromtimestamp(
                        _json.get("regularMarketTime")
                    ),
                    "exchange": _json.get("exchange"),
                }
            )

    def price_history(self, days_back, frequency):
        dataframes = []
        dt = timedelta(days=days_back)
        frequency = {"m": "mo", "w": "wk", "d": "d"}[frequency]

        now = datetime.utcnow()
        dateto = int(now.timestamp())
        datefrom = int((now - dt).timestamp())

        for symbol in self.symbols:
            url = self.history_url.format(symbol)
            params = {
                "period1": datefrom,
                "period2": dateto,
                "interval": f"1{frequency}",
                "events": "history",
            }
            param_string = urlencode(params).replace("%5Cu002F", "/")

            res = self._get(url, params=param_string)
            res.raise_for_status()

            df = pd.read_csv(StringIO(res.text), parse_dates=["Date"])
            df.insert(0, "Ticker", symbol)
            dataframes.append(df)

        df = pd.concat(dataframes, axis=0).reset_index(drop=True)

        return df

    @property
    def price(self):
        self._update_quote()
        return pd.DataFrame(self._quote)
