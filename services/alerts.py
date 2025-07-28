def price_alert(last_price: float, current_price: float, threshold: float) -> bool:
    """
    Check if the price change percentage exceeds the threshold.
    Returns True if alert condition is met.
    """
    change = ((current_price - last_price) / last_price) * 100
    return abs(change) >= threshold
