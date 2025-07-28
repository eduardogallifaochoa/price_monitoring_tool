import pytest
import os
from services.price_fetcher import get_current_price, fetch_all_prices
from config.settings import CURRENCY_PAIRS

# Detect if we are in CI (GitHub Actions sets CI=true)
IS_CI = os.getenv("CI") == "true"

@pytest.mark.skipif(IS_CI, reason="Skipping live API test in CI environment")
def test_get_current_price_live():
    """
    Test that Binance API returns a positive float for BTC price.
    """
    price = get_current_price("BTCUSDT")
    assert isinstance(price, float)
    assert price > 0

@pytest.mark.skipif(IS_CI, reason="Skipping live API test in CI environment")
def test_fetch_all_prices_live():
    """
    Test that all configured currency pairs return valid prices.
    """
    prices = fetch_all_prices()
    assert isinstance(prices, dict)
    for symbol in CURRENCY_PAIRS:
        assert symbol in prices
        assert isinstance(prices[symbol], float)
        assert prices[symbol] > 0

# --- Test mock ---
@pytest.mark.parametrize("mock_price", [25000.0, 30000.5])
def test_mock_price(monkeypatch, mock_price):
    """
    Test with mocked response for get_current_price.
    """
    import services.price_fetcher

    def mock_get_current_price(symbol):
        return mock_price

    monkeypatch.setattr(services.price_fetcher, "get_current_price", mock_get_current_price)
    price = services.price_fetcher.get_current_price("BTCUSDT")
    assert price == mock_price
