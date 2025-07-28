import sqlite3
from datetime import datetime, UTC
from typing import Dict

DB_NAME = "price_data.db"

def init_db():
    """
    Initialize SQLite database with a prices table if it doesn't exist.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            symbol TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_prices(data: Dict[str, float]):
    """
    Save current prices into the database.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    for symbol, price in data.items():
        cursor.execute("INSERT INTO prices (timestamp, symbol, price) VALUES (?, ?, ?)",
                       (timestamp, symbol, price))
    conn.commit()
    conn.close()

def get_last_price(symbol: str) -> float:
    """
    Fetch the most recent price for a given symbol from the database.
    Returns None if there is no data.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT price FROM prices WHERE symbol = ? ORDER BY id DESC LIMIT 1", (symbol,))
    result = cursor.fetchone()
    conn.close()
    return float(result[0]) if result else None

def get_all_prices(symbol: str, limit: int = 10):
    """
    Fetch the last N prices for a given symbol.
    Returns a list of (timestamp, price) tuples.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT timestamp, price FROM prices WHERE symbol = ? ORDER BY id DESC LIMIT ?",
        (symbol, limit)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows
