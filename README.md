# arkfunds-python

A Python library for monitoring [Ark Invest funds](https://ark-funds.com/) data.

## Installation
Install the latest release from [PyPI](https://pypi.org/project/arkfunds/):

```bash
pip install arkfunds
```

## Quickstart
```python
from arkfunds import ETF, Stock

# ARK ETFs
arkk = ETF('ARKK')

arkk.profile()
arkk.holdings()
arkk.trades()
arkk.news()

# Stocks
tsla = Stock("TSLA")

tsla.profile()
tsla.fund_ownership()
tsla.trades()

tsla.price()
tsla.price_history()
tsla.change()
tsla.changep()
tsla.last_trade()
```

## Usage: ARK ETFs
```python
from arkfunds import ETF
arkk = ETF('<ark fund symbols>')
```

### ETF Profile
```python
import json
from arkfunds import ETF
etfs = ETF("ARKF, ARKK, ARKX")

df = etfs.profile()
print(df)

# Output:
#   symbol                                name                                        description          fund_type inception_date      cusip          isin                            website
# 0   ARKF              Fintech Innovation ETF  ARKF is an actively managed Exchange Traded Fu...  Active Equity ETF     2019-02-04  00214Q708  US00214Q7088  https://ark-funds.com/fintech-etf
# 1   ARKK                  ARK Innovation ETF  ARKK is an actively managed ETF that seeks lon...  Active Equity ETF     2014-10-31  00214Q104  US00214Q1040         https://ark-funds.com/arkk
# 2   ARKX  Space Exploration & Innovation ETF  ARKX is an actively-managed exchange-traded fu...  Active Equity ETF     2021-03-30  00214Q807  US00214Q8078         https://ark-funds.com/arkx
```

### ETF Holdings
```python
from arkfunds import ETF
arkk = ETF('ARKK')

df = arkk.holdings()
print(df.head(5))

# Output:
#           date  fund                       company ticker      cusip     shares  market_value  weight  weight_rank
# 0   2021-07-23  ARKK                     TESLA INC   TSLA  88160R101    3598676  2.336476e+09   10.08            1
# 1   2021-07-23  ARKK                      ROKU INC   ROKU  77543R102    3243131  1.364223e+09    5.88            2
# 2   2021-07-23  ARKK            TELADOC HEALTH INC   TDOC  87918A105    8587318  1.312743e+09    5.66            3
# 3   2021-07-23  ARKK                SQUARE INC - A     SQ  852234103    4626083  1.205511e+09    5.20            4
# 4   2021-07-23  ARKK         SHOPIFY INC - CLASS A   SHOP  82509L107     717382  1.143571e+09    4.93            5
```

### ETF Trades
```python
from arkfunds import ETF
arkk = ETF('ARKK')

df = arkk.trades()
print(df)

# Output:
#           date  fund direction ticker                                company      cusip   shares  etf_percent
# 0   2021-07-23  ARKK       Buy      U                     UNITY SOFTWARE INC  91332U101    23749       0.0106
# 1   2021-07-23  ARKK       Buy   FATE                  FATE THERAPEUTICS INC  31189P102    74121       0.0270
# 2   2021-07-23  ARKK       Buy   TWTR                            TWITTER INC  90184L102   982205       0.2983
# 3   2021-07-23  ARKK       Buy   PACB  PACIFIC BIOSCIENCES OF CALIFORNIA INC  69404D108   265173       0.0345
# 4   2021-07-23  ARKK       Buy   PATH                             UIPATH INC  90364P105    80566       0.0217
# 5   2021-07-23  ARKK      Sell    TXG                       10X GENOMICS INC  88025U109    19665       0.0155
# 6   2021-07-23  ARKK      Sell   TWST                  TWIST BIOSCIENCE CORP  90184D100     5672       0.0029
# 7   2021-07-23  ARKK      Sell  TCEHY                   TENCENT HOLDINGS LTD  88032Q109      134       0.0000
# 8   2021-07-23  ARKK      Sell   ROKU                               ROKU INC  77543R102    59042       0.1180
# 9   2021-07-23  ARKK      Sell   PSTG                       PURE STORAGE INC  74624M102      350       0.0000
# 10  2021-07-23  ARKK      Sell    NVS                            NOVARTIS AG  66987V109      216       0.0001
# 11  2021-07-23  ARKK      Sell   DOCU                           DOCUSIGN INC  256163106    39242       0.0519
# 12  2021-07-23  ARKK      Sell   BEKE                        KE HOLDINGS INC  482497104  2033197       0.2549
```

### ETF News
```python
from arkfunds import ETF
arkk = ETF('ARKK')

df = arkk.news()
print(df.head(5))

# Output: 
#      id                   datetime related  ...                                            summary                                                url                                              image
# 0  2101  2021-07-23T08:42:00+00:00    ARKK  ...  One of Cathie Wood's ARK Invest funds bought o...  https://247wallst.com/investing/2021/07/23/cat...  https://247wallst.com/wp-content/uploads/2020/...
# 1  2102  2021-07-23T06:39:00+00:00    ARKK  ...                                                     https://www.gurufocus.com/news/1483143/cra-fin...                                                   
# 2  2095  2021-07-22T13:42:00+00:00    ARKK  ...  Ark Invest founder and CEO Cathie Wood achieve...  https://www.benzinga.com/news/21/07/22110608/e...  https://cdn.benzinga.com/files/imagecache/og_i...
# 3  2103  2021-07-22T11:10:00+00:00    ARKK  ...  When it comes to innovation and making your wo...  https://investorplace.com/2021/07/7-best-etfs-...  https://investorplace.com/wp-content/uploads/2...
# 4  2090  2021-07-22T10:51:00+00:00    ARKK  ...  The coronavirus pandemic is fast becoming one ...  https://www.marketwatch.com/story/biden-says-c...           https://images.mktw.net/im-373488/social
#
# [5 rows x 8 columns]                                                 
```

## Usage: Stocks
```python
from arkfunds import Stock
stock = Stock('<symbol>')
```

### Stock Profile
```python
import json
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.profile()
print(df)
print(df.columns.to_list())

# Output:
#   ticker         name        country            industry             sector  fullTimeEmployees  ...               website     market  exchange currency     marketCap  sharesOutstanding
# 0   TSLA  Tesla, Inc.  United States  Auto Manufacturers  Consumer Cyclical              70757  ...  http://www.tesla.com  us_market  NasdaqGS      USD  6.232552e+11          963329984
# 
# [1 rows x 13 columns]
#
# ['ticker', 'name', 'country', 'industry', 'sector', 'fullTimeEmployees', 'summary', 'website', 'market', 'exchange', 'currency', 'marketCap', 'sharesOutstanding']
```

### Stock Fund Ownership
```python
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.fund_ownership()
print(df)

# Output:
#          date ticker  fund  weight  weight_rank   shares  market_value
# 0  2021-07-23   TSLA  ARKK   10.08            1  3598676  2.336476e+09
# 1  2021-07-23   TSLA  ARKQ   11.02            1   482989  3.135854e+08
# 2  2021-07-23   TSLA  ARKW   10.10            1   913753  5.932633e+08
```

### Stock Trades
```python
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.trades()
print(df)

# Output:
#           date  fund direction ticker    company      cusip  shares  etf_percent
# 0   2021-07-07  ARKK       Buy   TSLA  TESLA INC  88160R101  110731       0.2941
# 1   2021-06-04  ARKK       Buy   TSLA  TESLA INC  88160R101    4977       0.0144
# 2   2021-06-04  ARKQ       Buy   TSLA  TESLA INC  88160R101    3068       0.0612
# 3   2021-06-04  ARKW       Buy   TSLA  TESLA INC  88160R101    4718       0.0521
# 4   2021-05-19  ARKK       Buy   TSLA  TESLA INC  88160R101   43065       0.1220
# ..         ...   ...       ...    ...        ...        ...     ...          ...
# 66  2020-09-24  ARKQ       Buy   TSLA  TESLA INC  88160R101    2639       0.1582
# 67  2020-09-24  ARKW       Buy   TSLA  TESLA INC  88160R101   19794       0.3054
# 68  2020-09-23  ARKK       Buy   TSLA  TESLA INC  88160R101  142166       0.6770
# 69  2020-09-23  ARKW       Buy   TSLA  TESLA INC  88160R101   22190       0.3682
# 70  2020-09-18  ARKK      Sell   TSLA  TESLA INC  88160R101   85200       0.4400
# 
# [71 rows x 8 columns]
```

### Stock Prices
```python
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.price()
print(df)
# Output:
#   ticker currency   price    change   changep          last_trade exchange
# 0   TSLA      USD  646.98  2.199951  0.341194 2021-07-28 20:00:03      NMS

df = tsla.price_history(days_back=7, frequency="d")
print(df)

# Output: 
#         Date        Open        High         Low       Close   Adj Close    Volume
# 0 2021-07-21  659.609985  664.859985  650.289978  655.289978  655.289978  13910800
# 1 2021-07-22  656.440002  662.169983  644.599976  649.260010  649.260010  15105700
# 2 2021-07-23  646.359985  648.799988  637.299988  643.380005  643.380005  14581300
# 3 2021-07-26  650.969971  668.200012  647.109985  657.619995  657.619995  25044100
# 4 2021-07-27  663.400024  666.500000  627.239990  644.780029  644.780029  32756900
# 5 2021-07-28  646.994995  654.969910  639.400085  646.979980  646.979980  15790823
```

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
