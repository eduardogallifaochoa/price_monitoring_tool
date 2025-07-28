import sqlite3

DB_NAME = "price_data.db"

def view_last_prices(limit=10):
    """
    Print the last N rows from the prices table.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("SELECT timestamp, symbol, price FROM prices ORDER BY id DESC LIMIT ?", (limit,))
        rows = cursor.fetchall()
        conn.close()

        if not rows:
            print("No data found in the database.")
            return

        print(f"Last {limit} price records:")
        for row in rows:
            print(f"Timestamp: {row[0]} | Symbol: {row[1]} | Price: {row[2]}")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    view_last_prices(10)
