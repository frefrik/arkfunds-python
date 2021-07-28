from arkfunds import ETF, Stock
from pprint import pprint

"""
tsla = Stock("TSLA")
price = tsla.price()
change = tsla.change()
changep = tsla.changep()
last_trade = tsla.last_trade()
price_history = tsla.price_history(days_back=7, frequency="d")
print("price", price)
print("change", change)
print("changep", changep)
print("last_trade", last_trade)
print(price_history)
"""

# etf = ETF("ARKF, ARKK, ARKX")
# print(etf.profile())
# print(etf.news())

tsla = Stock("tsla")

profile = tsla.price()
print(profile)


# etf.validation()


"""
arkk = ETF("ARKK")

holdings = arkk.holdings()
profile = arkk.profile()
trades = arkk.trades()
news = arkk.news(date_from="2021-07-22")

# print(news)

# print(profile)
print(holdings)
print(trades)
print(news)


# stock_profile = ark.stock_profile(symbol="TSLA", output="df")
# stock_fund_ownership = ark.stock_fund_ownership(symbol="TSLA", output="df")
# stock_trades = ark.stock_trades(symbol="TSLA", direction="Sell")

tsla = Stock("TSLA")

profile = tsla.profile()
fund_ownership = tsla.fund_ownership()
trades = tsla.trades(direction="Buy")

# pprint(profile)
print(fund_ownership)
print(trades)
"""
