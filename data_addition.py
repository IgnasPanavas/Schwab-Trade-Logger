import json
from datetime import datetime
from models import Trade  # Assuming you have the Trade model defined
from db_manager import get_db_session  # Assuming your session context manager is in get_db_session.py
import re
from datetime import datetime

from models.TradeGroups import TradeGroup

def extract_date(date_str):
    """
    Extracts the date in MM/DD/YYYY format from a string that may contain extra text.
    """
    # Use a regular expression to match a date in MM/DD/YYYY format
    match = re.search(r'\d{2}/\d{2}/\d{4}', date_str)
    if match:
        # Parse the matched date
        return datetime.strptime(match.group(), '%m/%d/%Y')
    else:
        raise ValueError(f"Could not find a valid date in the string: {date_str}")

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

            # Remove dollar signs and commas from Price and Amount
            price_str = trade_data['Price'].replace('$', '').replace(',', '').strip()
            amount_str = trade_data['Amount'].replace('$', '').replace(',', '').replace('(', '-').replace(')', '').strip()
            fees_commission_str = trade_data.get('Fees & Comm', '0').replace('$', '').replace(',', '').strip()

            # Handle empty or missing price
            price = float(price_str) if price_str else 0.0
            amount = float(amount_str) if amount_str else 0.0
            fees_commission = float(fees_commission_str) if fees_commission_str else 0.0

            # Parse the quantity as a float and round it to the nearest integer
            quantity_str = trade_data['Quantity'].replace(',', '').strip()
            quantity = round(float(quantity_str)) if quantity_str else 0  # Round to nearest integer

            # Extract and parse the trade date (handles extra text)
            trade_date = extract_date(trade_data['Date'])

            # Ensure the trade belongs to a TradeGroup (either fetch or create a new one)
            symbol = trade_data['Symbol']
            trade_group = session.query(TradeGroup).filter_by(symbol=symbol).first()
            
            # If the trade group doesn't exist, create one
            if not trade_group:
                trade_group = TradeGroup(symbol=symbol, total_quantity=quantity, open_quantity=quantity, status='open')
                session.add(trade_group)
                session.flush()  # Flush to get the trade_group_id before inserting trades

            # Create a Trade object
            trade = Trade(
                trade_group_id=trade_group.trade_group_id,  # Assign the trade_group_id
                trade_date=trade_date,
                action=trade_data['Action'],
                symbol=symbol,
                description=trade_data['Description'],
                contracts=quantity,  # Rounded quantity stored as an integer
                price=price,
                total_cost=amount,
                commission=fees_commission
            )

            # Add the trade to the session
            session.add(trade)

        # Commit all trades to the database
        session.commit()

add_trades_to_db(parse_json("transactions.json"))