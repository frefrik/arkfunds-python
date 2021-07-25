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

## Usage: ARK ETFs
```python
from arkfunds import ETF
arkk = ETF('<ark fund symbol>')
```

### ETF Profile
```python
import json
from arkfunds import ETF
arkk = ETF('ARKK')

profile = arkk.profile()
print(json.dumps(profile, indent=2))

# Output:
# [
#   {
#     "symbol": "ARKK",
#     "name": "ARK Innovation ETF",
#     "description": "ARKK is an actively managed ETF that seeks long-term growth of capital by investing under normal circumstances primarily (at least 65% of its assets) in domestic and foreign equity securities of companies that are relevant to the Fund's investment theme of disruptive innovation.",
#     "fund_type": "Active Equity ETF",
#     "inception_date": "2014-10-31",
#     "cusip": "00214Q104",
#     "isin": "US00214Q1040",
#     "website": "https://ark-funds.com/arkk"
#   }
# ]
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

### ETF Prices
```python
from arkfunds import ETF
arkk = ETF('ARKK')

p = arkk.price()
print(p)
# Output:
# 122.43

c = arkk.change()
print(c)
# Output:
# 0.7200012

cp = arkk.changep()
print(cp)
# Output:
# 0.5915711

lt = arkk.last_trade()
print(lt)
# Output:
# datetime.datetime(2021, 7, 23, 20, 0)

df = arkk.price_history(days_back=7, frequency="d")
print(df)

# Output: 
#         Date        Open        High         Low       Close   Adj Close    Volume
# 0 2021-07-19  113.919998  117.580002  113.269997  117.279999  117.279999  11861800
# 1 2021-07-20  117.510002  121.175003  116.449997  120.760002  120.760002   6707700
# 2 2021-07-21  120.875000  122.910004  119.980003  122.660004  122.660004   5738200
# 3 2021-07-22  122.500000  123.419998  121.250000  121.709999  121.709999   4781500
# 4 2021-07-23  122.000000  122.559998  120.379997  122.430000  122.430000   4383900
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

profile = tsla.profile()
print(json.dumps(profile, indent=2))

# Output:
# {
#   "ticker": "TSLA",
#   "name": "Tesla, Inc.",
#   "country": "United States",
#   "industry": "Auto Manufacturers",
#   "sector": "Consumer Cyclical",
#   "fullTimeEmployees": 70757,
#   "summary": "Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems in the United States, China, and internationally. The company operates in two segments, Automotive, and Energy Generation and Storage. The Automotive segment offers electric vehicles, as well as sells automotive regulatory credits. It provides sedans and sport utility vehicles through direct and used vehicle sales, a network of Tesla Superchargers, and in-app upgrades; and purchase financing and leasing services. This segment is also involved in the provision of non-warranty after-sales vehicle services, sale of used vehicles, retail merchandise, and vehicle insurance, as well as sale of products through its subsidiaries to third party customers; services for electric vehicles through its company-owned service locations, and Tesla mobile service technicians; and vehicle limited warranties and extended service plans. The Energy Generation and Storage segment engages in the design, manufacture, installation, sale, and leasing of solar energy generation and energy storage products, and related services to residential, commercial, and industrial customers and utilities through its website, stores, and galleries, as well as through a network of channel partners. This segment also offers service and repairs to its energy product customers, including under warranty; and various financing options to its solar customers. The company was formerly known as Tesla Motors, Inc. and changed its name to Tesla, Inc. in February 2017. Tesla, Inc. was founded in 2003 and is headquartered in Palo Alto, California.",
#   "website": "http://www.tesla.com",
#   "market": "us_market",
#   "exchange": "NasdaqGS",
#   "currency": "USD",
#   "marketCap": 619787255808.0,
#   "sharesOutstanding": 963329984
# }
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

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
