import pytest
from services.alerts import price_alert

def test_price_alert_triggered_positive_change():
    """
    Test that price_alert triggers when price increases beyond threshold.
    """
    last_price = 100.0
    current_price = 105.0
    threshold = 4.0  # 5% change > 4% threshold
    assert price_alert(last_price, current_price, threshold) is True

def test_price_alert_triggered_negative_change():
    """
    Test that price_alert triggers when price decreases beyond threshold.
    """
    last_price = 100.0
    current_price = 90.0
    threshold = 5.0  # 10% drop > 5% threshold
    assert price_alert(last_price, current_price, threshold) is True

def test_price_alert_not_triggered():
    """
    Test that price_alert does not trigger when change is within threshold.
    """
    last_price = 100.0
    current_price = 101.0
    threshold = 5.0  # 1% change < 5% threshold
    assert price_alert(last_price, current_price, threshold) is False
