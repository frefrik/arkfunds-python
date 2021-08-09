import importlib.metadata

from .etf import ETF
from .stock import Stock

__version__ = importlib.metadata.version("arkfunds")
