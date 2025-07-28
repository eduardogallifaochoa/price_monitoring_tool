import os
import sqlite3
import pytest
from services import db_storage

TEST_DB = "test_price_data.db"

@pytest.fixture(scope="function")
def setup_test_db():
    """
    Create a clean test database before each test.
    """
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)
    conn = sqlite3.connect(TEST_DB)
    conn.execute("""
        CREATE TABLE prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT NOT NULL,
            symbol TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)
    conn.close()
    yield
    if os.path.exists(TEST_DB):
        os.remove(TEST_DB)

def test_save_and_get_prices(setup_test_db, monkeypatch):
    monkeypatch.setattr(db_storage, "DB_NAME", TEST_DB)
    db_storage.save_prices({"BTCUSDT": 30000.0, "ETHUSDT": 2000.0})
    last_price = db_storage.get_last_price("BTCUSDT")
    assert last_price == 30000.0
    rows = db_storage.get_all_prices("ETHUSDT")
    assert len(rows) == 1
    assert rows[0][1] == 2000.0
