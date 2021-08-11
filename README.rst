arkfunds-python
===============

.. image:: https://badge.fury.io/py/arkfunds.svg
   :target: https://badge.fury.io/py/arkfunds
   :alt: PyPI version
.. image:: https://img.shields.io/github/license/frefrik/arkfunds-python
   :target: LICENSE
   :alt: Project Licence


A Python library for monitoring `Ark Invest <https://ark-funds.com/>`_ funds data.

Installation
------------

Install the latest release from `PyPI <https://pypi.org/project/arkfunds/>`_\ :

.. code-block:: console

   pip install arkfunds

Quickstart
----------

.. code-block:: python

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

Getting Started
---------------
See our `Getting started guide <https://arkfunds-python.readthedocs.io/en/latest/getting-started.html>`_ in the documentation.

License
-------

This project is licensed under the **MIT license**. Feel free to edit and distribute this template as you like.

See `LICENSE <LICENSE>`_ for more information.
