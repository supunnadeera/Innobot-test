# /utils/csv_writer.py
import csv
import os

class CSVWriter:
    def __init__(self, filename):
        self.filename = filename
        # Check if file exists; if not, write the headers
        if not os.path.exists(self.filename):
            self._write_headers()

    def _write_headers(self):
        """Writes the headers to the CSV file."""
        with open(self.filename, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Location", "Seller Badge"])
            writer.writeheader()

    def write_data(self, data_list):
        """Writes a list of ad data to the CSV file."""
        with open(self.filename, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=["Title", "Price", "Location", "Seller Badge"])
            writer.writerows(data_list)
