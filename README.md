# python-arkfunds

python-arkfunds is a Python library for monitoring Ark Invest funds data.

## Usage
```python
from arkfunds import ETF, Stock

# ARK ETFs
arkk = ETF('ARKK')

arkk.profile()
arkk.holdings()
arkk.trades()
arkk.news()

arkk.price()
arkk.price_history()
arkk.change()
arkk.changep()
arkk.last_trade()

# Stocks
tsla = Stock("TSLA")

tsla.profile()
tsla.fund_ownership()
tsla.trades()
```