import importlib.metadata
import re


def get_useragent(client, agent="Mozilla/5.0"):
    if client == "ArkFunds":
        ver = importlib.metadata.version("arkfunds")
        agent = f"python-arkfunds/{ver}"

    return agent


def _convert_to_list(symbols, comma_split=False):
    if isinstance(symbols, str):
        if comma_split:
            return [x.strip() for x in symbols.upper().split(",")]
        else:
            return re.findall(r"[\w\-.=^&]+", symbols.upper())
    return [symbol.upper() for symbol in symbols]
