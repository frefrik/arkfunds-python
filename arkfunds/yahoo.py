from datetime import datetime, timedelta
from io import StringIO
from urllib.parse import urlencode

import pandas as pd
import requests

from .utils import get_useragent


class YahooFinance:
    quote_url = "https://query2.finance.yahoo.com/v7/finance/options/{0}"
    history_url = "https://query1.finance.yahoo.com/v7/finance/download/{0}"

    _COLUMNS = {
        "price": [
            "ticker",
            "currency",
            "price",
            "change",
            "changep",
            "last_trade",
            "exchange",
        ],
        "price_history": [
            "ticker",
            "date",
            "open",
            "high",
            "low",
            "close",
            "adj_close",
            "volume",
        ],
    }

    def __init__(self, symbols):
        self.symbols = symbols
        self.timeout = 2
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": get_useragent(__class__.__name__)})

    def _get_data(self, url, params=None):
        res = self.session.get(url, params=params, timeout=self.timeout)

        if res.status_code == 404:
            return None

        res.raise_for_status()

        return res

    def _update_quote(self):
        self._quote = []
        for symbol in self.symbols:
            res = self._get_data(self.quote_url.format(symbol))

            _json = res.json()["optionChain"]["result"]

            if len(_json) > 0:
                _data = _json[0]["quote"]

                self._quote.append(
                    {
                        "ticker": _data.get("symbol"),
                        "currency": _data.get("currency"),
                        "price": _data.get("regularMarketPrice"),
                        "change": _data.get("regularMarketChange"),
                        "changep": _data.get("regularMarketChangePercent"),
                        "last_trade": datetime.utcfromtimestamp(
                            _data.get("regularMarketTime")
                        ),
                        "exchange": _data.get("exchange"),
                    }
                )

    def price_history(self, days_back, frequency):
        df = pd.DataFrame(columns=self._COLUMNS["price_history"])
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
            res = self._get_data(url, params=param_string)

            if res:
                df = pd.read_csv(StringIO(res.text), parse_dates=["Date"])
                df.insert(0, "ticker", symbol)
                df.columns = self._COLUMNS["price_history"]
                dataframes.append(df)

        if df.empty:
            return f"Stock.price_history: No data found for {self.symbols}"
        else:
            return pd.concat(dataframes, axis=0).reset_index(drop=True)

    @property
    def price(self):
        self._update_quote()
        df = pd.DataFrame(self._quote, columns=self._COLUMNS["price"])

        if df.empty:
            return f"Stock.price: No data found for {self.symbols}"
        else:
            return df
