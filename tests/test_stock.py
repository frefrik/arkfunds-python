import pytest
from arkfunds import Stock
from requests.exceptions import HTTPError

STOCKS = [
    Stock("TSLA"),
    Stock("tsla, coin"),
    Stock("tdoc, aapl, tsla"),
    Stock("roku SHOP tsla"),
    Stock(["TSLA", "sq", "TDOC", "spot"]),
]


@pytest.fixture(params=STOCKS)
def stock(request):
    return request.param


def test_stock_profile(stock):
    assert not stock.profile().empty


def test_stock_profile_columns(stock):
    columns = [
        "ticker",
        "name",
        "country",
        "industry",
        "sector",
        "fullTimeEmployees",
        "summary",
        "website",
        "market",
        "exchange",
        "currency",
        "marketCap",
        "sharesOutstanding",
    ]
    assert stock.profile().columns.to_list() == columns


def test_bad_stock_profile(symbol="TSLAS"):
    with pytest.raises(HTTPError):
        assert Stock(symbol).profile()


def test_stock_fund_ownership(stock):
    assert stock.fund_ownership() is not None


def test_stock_trades(stock):
    assert not stock.trades().empty


def test_stock_price(stock):
    assert not stock.price().empty


def test_stock_price_history(stock):
    assert not stock.price_history().empty


def test_stock_symbols_list():
    symbols = [
        "tsla, aapl, tdoc",
        "tsla aapl tdoc",
        ["tsla", "aapl", "tdoc"],
    ]
    for symbol in symbols:
        stock = Stock(symbol)
    assert stock.symbols == ["TSLA", "AAPL", "TDOC"]
