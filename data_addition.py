import json
from datetime import datetime
from db_functions import add_trade
from models import Trade  # Assuming you have the Trade model defined
from db_manager import get_db_session  # Assuming your session context manager is in get_db_session.py
import re
from datetime import datetime

from models.TradeGroups import TradeGroup


def parse_json(file_path):
    """
    Reads and parses the JSON file.
    """
    with open(file_path, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)
        
        # Get the transactions
        transactions = data['BrokerageTransactions']
        return transactions
    
def add_trades_to_db(transactions):
    """
    Add the trades from JSON to the database, ensuring trade_group_id is assigned.
    """
    # Define a list of actions to exclude
    actions_to_exclude = ['MoneyLink', 'ACH Transfer', 'Dividend', 'Interest']  # Add any other actions you want to exclude

    with get_db_session() as session:
        for trade_data in transactions:
            # Skip the transaction if the action is in the exclude list
            if trade_data['Action'] in actions_to_exclude:
                print(f"Skipping transaction with Action: {trade_data['Action']}")
                continue  # Skip to the next transaction

            add_trade(trade_data)

add_trades_to_db(parse_json("transactions.json"))