import time
from services.price_fetcher import fetch_all_prices
from services.storage import save_to_csv
from services.db_storage import init_db, save_prices
from config.settings import INTERVAL, ALERT_THRESHOLD_PERCENT, CURRENCY_PAIRS
from services.alerts import price_alert

def main():
    """
    Entry point for the Price Monitoring Tool.
    Fetches prices, checks alerts, and stores data in CSV and SQLite.
    """
    print("Starting Price Monitoring Tool with SQLite support...")
    print("Press Ctrl + C to stop the monitoring loop.")
    init_db()
    last_prices = {symbol: None for symbol in CURRENCY_PAIRS}
    csv_file = "price_data.csv"

    try:
        while True:
            current_prices = fetch_all_prices()
            print(f"Current Prices: {current_prices}")

            for symbol, price in current_prices.items():
                if last_prices[symbol] is not None:
                    if price_alert(last_prices[symbol], price, ALERT_THRESHOLD_PERCENT):
                        print(f"ALERT: {symbol} changed significantly! ({last_prices[symbol]} -> {price})")
                last_prices[symbol] = price

            save_to_csv(csv_file, current_prices)
            save_prices(current_prices)
            time.sleep(INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user.")

if __name__ == "__main__":
    main()
