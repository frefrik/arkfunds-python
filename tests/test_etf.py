import pytest

from arkfunds import ETF

ETFS = [
    ETF("ARKX"),
    ETF("arkk, prnt, izrl"),
    ETF("arkk, arkg, arkx, IZRL"),
    ETF("arkk ARKF arkg ARKX izrl"),
    ETF(["ARKK", "arkf", "arkg", "arkx", "izrl"]),
]


@pytest.fixture(params=ETFS)
def etf(request):
    return request.param


def test_etf_profile(etf):
    assert not etf.profile().empty


def test_etf_holdings(etf):
    assert not etf.holdings().empty


def test_etf_trades(etf):
    assert not etf.trades().empty


def test_etf_news(etf):
    assert not etf.news().empty


def test_bad_etf_symbols(symbols="ARKK, ARKF, ARKS"):
    with pytest.raises(ValueError):
        assert ETF(symbols)


def test_etf_symbols_list():
    symbols = [
        "arkk, arkf, arkg, arkx, izrl",
        "arkk arkf arkg arkx izrl",
        ["arkk", "arkf", "arkg", "arkx", "izrl"],
    ]
    for symbol in symbols:
        etf = ETF(symbol)

    assert etf.symbols == ["ARKK", "ARKF", "ARKG", "ARKX", "IZRL"]
