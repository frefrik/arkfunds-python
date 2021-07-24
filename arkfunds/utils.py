import importlib.metadata


def get_useragent(client, agent="Mozilla/5.0"):
    if client == "ArkFunds":
        ver = importlib.metadata.version("arkfunds")
        agent = f"python-arkfunds/{ver}"

    return agent
