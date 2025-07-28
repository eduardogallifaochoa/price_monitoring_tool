import os
import csv
from services.storage import save_to_csv

TEST_CSV = "test_price_data.csv"

def setup_function():
    """
    Remove test CSV file before each test.
    """
    if os.path.exists(TEST_CSV):
        os.remove(TEST_CSV)

def teardown_function():
    """
    Clean up test CSV file after each test.
    """
    if os.path.exists(TEST_CSV):
        os.remove(TEST_CSV)

def test_save_to_csv_creates_file():
    """
    Test that save_to_csv creates a CSV file with header.
    """
    data = {"BTCUSDT": 30000.0, "ETHUSDT": 2000.0}
    save_to_csv(TEST_CSV, data)
    assert os.path.exists(TEST_CSV)

def test_save_to_csv_adds_row():
    """
    Test that save_to_csv appends a row with correct values.
    """
    data = {"BTCUSDT": 30000.0, "ETHUSDT": 2000.0}
    save_to_csv(TEST_CSV, data)
    with open(TEST_CSV, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 1
        assert "timestamp" in rows[0]
        assert float(rows[0]["BTCUSDT"]) == 30000.0
        assert float(rows[0]["ETHUSDT"]) == 2000.0

def test_save_to_csv_appends_multiple_rows():
    """
    Test that multiple calls to save_to_csv append new rows.
    """
    data1 = {"BTCUSDT": 30000.0, "ETHUSDT": 2000.0}
    data2 = {"BTCUSDT": 31000.0, "ETHUSDT": 2100.0}
    save_to_csv(TEST_CSV, data1)
    save_to_csv(TEST_CSV, data2)
    with open(TEST_CSV, "r") as file:
        reader = csv.DictReader(file)
        rows = list(reader)
        assert len(rows) == 2
