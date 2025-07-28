import sqlite3

DB_NAME = "price_data.db"

def clear_database():
    """
    Delete all rows from the prices table in the SQLite database.
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM prices")
        conn.commit()
        conn.close()
        print("Database cleared successfully!")
    except sqlite3.Error as e:
        print(f"Database error: {e}")

if __name__ == "__main__":
    confirm = input("Are you sure you want to clear all data in price_data.db? (yes/no): ")
    if confirm.lower() == "yes":
        clear_database()
    else:
        print("Action canceled.")
