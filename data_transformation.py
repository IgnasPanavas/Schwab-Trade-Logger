import os
from dotenv import load_dotenv
import csv
from datetime import datetime
from models import Trade, TradeGroup  # Assuming your models are in models.py
from db_manager import get_db_session  # Assuming your context manager is in get_db_session.py

def parse_csv(file_path):
    trades = []

    # Open the CSV file
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate through the CSV rows
        for row in reader:
            # Parse relevant fields
            trade = {
                'date': datetime.strptime(row['Date'], '%m/%d/%Y'),
                'action': row['Action'],
                'symbol': row['Symbol'],
                'description': row['Description'],
                'quantity': int(row['Quantity']),
                'price': float(row['Price'].replace('$', '').replace(',', '')),
                'fees_commission': float(row.get('Fees & Comm', '0').replace('$', '').replace(',', '')) if row.get('Fees & Comm') else 0,
                'amount': float(row['Amount'].replace('$', '').replace(',', '').replace('(', '-').replace(')', '')),
            }
            trades.append(trade)

    return trades
