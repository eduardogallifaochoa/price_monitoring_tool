import requests
from config.settings import API_BASE_URL, CURRENCY_PAIRS

def get_current_price(symbol: str) -> float:
    """
    Fetch the current price of a given currency pair from Binance API.
    """
    url = f"{API_BASE_URL}/ticker/price?symbol={symbol}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    return float(data["price"])

def fetch_all_prices() -> dict:
    """
    Fetch prices for all currency pairs defined in settings.
    Returns a dictionary with pair: price.
    """
    return {symbol: get_current_price(symbol) for symbol in CURRENCY_PAIRS}
