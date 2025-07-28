import csv
from datetime import datetime, UTC

def save_to_csv(file_path: str, data: dict):
    """
    Append price data with timestamp to a CSV file.
    If file does not exist, create it and add a header.
    """
    fieldnames = ["timestamp"] + list(data.keys())
    timestamp = datetime.now(UTC).strftime("%Y-%m-%d %H:%M:%S")
    row = {"timestamp": timestamp, **data}

    file_exists = False
    try:
        with open(file_path, "r"):
            file_exists = True
    except FileNotFoundError:
        pass

    with open(file_path, mode="a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)
