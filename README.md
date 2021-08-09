# arkfunds-python

A Python library for monitoring [Ark Invest](https://ark-funds.com/) funds data.

## Installation
Install the latest release from [PyPI](https://pypi.org/project/arkfunds/):

```bash
pip install arkfunds
```

## Quickstart
```python
from arkfunds import ETF, Stock

# ARK ETFs
etf = ETF("ARKK")

etf.profile()
etf.holdings()
etf.trades()
etf.news()

# Stocks
symbols = ["tsla", "coin", "tdoc"]
stock = Stock(symbols)

stock.profile()
stock.fund_ownership()
stock.trades()

stock.price()
stock.price_history()
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
symbols = ["ARKF", "ARKK", "ARKX"]
etfs = ETF(symbols)

df = etfs.profile()
print(df)

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

#    fund        date                company ticker      cusip   shares  market_value  weight  weight_rank
# 0  ARKK  2021-07-29              TESLA INC   TSLA  88160R101  3551176  2.297540e+09   10.14            1
# 1  ARKK  2021-07-29               ROKU INC   ROKU  77543R102  3094614  1.449362e+09    6.39            2
# 2  ARKK  2021-07-29     TELADOC HEALTH INC   TDOC  87918A105  8785584  1.333740e+09    5.88            3
# 3  ARKK  2021-07-29         SQUARE INC - A     SQ  852234103  4565037  1.180564e+09    5.21            4
# 4  ARKK  2021-07-29  SHOPIFY INC - CLASS A   SHOP  82509L107   707932  1.088799e+09    4.80            5
```

### ETF Trades
```python
from arkfunds import ETF
arkk = ETF('ARKK')

df = arkk.trades()
print(df)

#     fund        date direction ticker                      company      cusip  shares  etf_percent
# 0   ARKK  2021-07-28       Buy   TDOC           TELADOC HEALTH INC  87918A105  311612       0.2043
# 1   ARKK  2021-07-28       Buy   SPOT        SPOTIFY TECHNOLOGY SA  L8681T102  201549       0.1966
# 2   ARKK  2021-07-28      Sell   BEKE              KE HOLDINGS INC  482497104   41500       0.0052
# 3   ARKK  2021-07-28      Sell   TWST        TWIST BIOSCIENCE CORP  90184D100   89660       0.0464
# 4   ARKK  2021-07-28      Sell   SKLZ                   SKILLZ INC  83067L109  921897       0.0592
# 5   ARKK  2021-07-28      Sell   ROKU                     ROKU INC  77543R102   47200       0.0987
# 6   ARKK  2021-07-28      Sell   PSTG             PURE STORAGE INC  74624M102      85       0.0000
# 7   ARKK  2021-07-28      Sell  NTDOY              NINTENDO CO LTD  654445303   25100       0.0076
# 8   ARKK  2021-07-28      Sell   IOVA  IOVANCE BIOTHERAPEUTICS INC  462260100  413807       0.0427
# 9   ARKK  2021-07-28      Sell   DOCU                 DOCUSIGN INC  256163106   65768       0.0893
# 10  ARKK  2021-07-28      Sell    TXG             10X GENOMICS INC  88025U109   89643       0.0752
```

### ETF News
```python
from arkfunds import ETF
arkk = ETF('ARKK')

df = arkk.news()
print(df.head(5))
 
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
stock = Stock('<symbols>')
```

### Stock Profile
```python
import json
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.profile()
print(df)
print(df.columns.to_list())

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

#   ticker        date  fund  weight  weight_rank   shares  market_value
# 0   TSLA  2021-07-29  ARKK   10.14            1  3551176  2.297540e+09
# 1   TSLA  2021-07-29  ARKQ   11.33            1   478166  3.093638e+08
# 2   TSLA  2021-07-29  ARKW    9.87            1   898972  5.816169e+08
```

### Stock Trades
```python
from arkfunds import Stock
tsla = Stock('TSLA')

df = tsla.trades()
print(df)

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
symbols = ["tsla", "coin", "tdoc"]
stock = Stock(symbols)

df = stock.price()
print(df)

#   ticker currency   price    change   changep          last_trade exchange
# 0   TSLA      USD  646.98  2.199951  0.341194 2021-07-28 20:00:03      NMS
# 1   COIN      USD  241.75  6.669998  2.837331 2021-07-28 20:00:02      NMS
# 2   TDOC      USD  151.81  0.800003  0.529768 2021-07-28 20:00:02      NYQ

df = stock.price_history(days_back=7, frequency="d")
print(df)
 
#    Ticker       Date        Open        High         Low       Close   Adj Close    Volume
# 0    TSLA 2021-07-22  656.440002  662.169983  644.599976  649.260010  649.260010  15105700
# 1    TSLA 2021-07-23  646.359985  648.799988  637.299988  643.380005  643.380005  14581300
# 2    TSLA 2021-07-26  650.969971  668.200012  647.109985  657.619995  657.619995  25044100
# 3    TSLA 2021-07-27  663.400024  666.500000  627.239990  644.780029  644.780029  32756900
# 4    TSLA 2021-07-28  647.000000  654.969971  639.400024  646.979980  646.979980  15970200
# 5    COIN 2021-07-22  232.000000  232.320007  224.500000  226.080002  226.080002   2551700
# 6    COIN 2021-07-23  226.220001  227.350006  222.729996  224.919998  224.919998   1565900
# 7    COIN 2021-07-26  240.080002  249.800003  237.880005  245.449997  245.449997   7592500
# 8    COIN 2021-07-27  243.000000  243.210007  229.119995  235.080002  235.080002   5615000
# 9    COIN 2021-07-28  240.300003  242.869995  238.029999  241.750000  241.750000   2057800
# 10   TDOC 2021-07-22  154.449997  155.369995  151.600006  152.869995  152.869995   1302300
# 11   TDOC 2021-07-23  151.949997  152.602997  147.860001  151.589996  151.589996   1629800
# 12   TDOC 2021-07-26  150.910004  150.919998  148.570007  149.750000  149.750000   2136300
# 13   TDOC 2021-07-27  149.929993  152.169998  145.619995  151.009995  151.009995   2714300
# 14   TDOC 2021-07-28  134.779999  152.289993  133.250000  151.809998  151.809998  11577300
```

## License

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See [LICENSE](LICENSE) for more information.
