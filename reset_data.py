import os
import sqlite3

DB_NAME = "price_data.db"
CSV_NAME = "price_data.csv"

def reset_data():
    # Clear database
    conn = sqlite3.connect(DB_NAME)
    conn.execute("DELETE FROM prices")
    conn.commit()
    conn.close()

    # Remove CSV
    if os.path.exists(CSV_NAME):
        os.remove(CSV_NAME)

    print("Database and CSV have been cleared!")

if __name__ == "__main__":
    confirm = input("Are you sure you want to reset all data (DB + CSV)? (yes/no): ")
    if confirm.lower() == "yes":
        reset_data()
    else:
        print("Action canceled.")
