import re
from datetime import datetime

from db_manager import get_db_session
from models import Trade
from models.TradeGroups import TradeGroup

def extract_date(date_string):
    primary_date = date_string.split(" as of ")[0]
    return datetime.strptime(primary_date, "%m/%d/%Y").date()

def clean_numeric(value):
    cleaned_value = re.sub(r'[^\d.-]', '', value)
    return float(cleaned_value) if cleaned_value else 0  # Default to 0 if empty

def clean_integer(value):
    cleaned_value = re.sub(r'[^\d-]', '', value)
    return int(cleaned_value) if cleaned_value else 0  # Default to 0 if empty

def create_trade_entry(trade_data, trade_group_id):
    """Helper function to create a Trade object from trade data."""
    return Trade(
        trade_group_id=trade_group_id,
        trade_date=extract_date(trade_data['Date']),
        action=trade_data['Action'],
        symbol=trade_data['Symbol'],
        description=trade_data['Description'],
        quantity=clean_integer(trade_data['Quantity']),
        price=clean_numeric(trade_data['Price']),
        amount=clean_numeric(trade_data['Amount']),
        commission=clean_numeric(trade_data['Fees & Comm']),
    )

def add_trade(trade_data):
    """Main function to route trade action to the correct handler."""
    with get_db_session() as session:
        action = trade_data['Action']
        
        if action in ('Buy', 'Sell to Open', 'Buy to Open'):
            add_opening_trade(trade_data, session)
        elif action in ('Sell', 'Sell to Close', 'Buy to Close'):
            add_closing_trade(trade_data, session)
        elif action == 'Expired':
            add_expired_trade(trade_data, session)
        else:
            print(f"Unrecognized action: {action}")

def add_opening_trade(trade_data, session):
    """Handles 'Buy', 'Sell to Open', and 'Buy to Open' actions."""
    # Create a new TradeGroup for opening trade
    quantity = clean_integer(trade_data['Quantity'])
    trade_group = TradeGroup(
        symbol=trade_data['Symbol'],
        total_quantity=quantity,
        open_quantity=quantity,  # All contracts are open initially
        status='open'  # Trade group is open
    )
    session.add(trade_group)
    session.commit()  # Commit to generate the trade_group_id

    # Create the Trade entry
    trade = create_trade_entry(trade_data, trade_group.trade_group_id)
    session.add(trade)
    session.commit()

    print(f"Opening trade added with trade_id: {trade.trade_id} and group_id: {trade_group.trade_group_id}")

def add_closing_trade(trade_data, session):
    """Handles 'Sell', 'Sell to Close', and 'Buy to Close' actions."""
    print("Detected closing trade...")

    # Find the corresponding TradeGroup
    trade_group = session.query(TradeGroup).filter(
        TradeGroup.symbol == trade_data['Symbol'],
        TradeGroup.status != 'closed'
    ).first()

    if not trade_group:
        print("No open trade group found for symbol. Cannot add closing trade.")
        return

    # Calculate the remaining open quantity
    quantity = clean_integer(trade_data['Quantity'])
    if trade_group.open_quantity >= abs(quantity):
        trade_group.open_quantity -= abs(quantity)

        # Update the status of the trade group
        trade_group.update_status()

        # Add the closing trade
        trade = create_trade_entry(trade_data, trade_group.trade_group_id)
        session.add(trade)
        session.commit()

        print(f"Closing trade added with trade_id: {trade.trade_id} for group_id: {trade_group.trade_group_id}")
    else:
        print("Error: Closing more contracts than open in the trade group.")

def add_expired_trade(trade_data, session):
    """Handles 'Expired' action."""
    print("Detected expired trade...")

    # No need to modify trade group quantities; just log the expiration.
    trade_group = session.query(TradeGroup).filter(
        TradeGroup.symbol == trade_data['Symbol'],
        TradeGroup.status != 'closed'
    ).first()

    if not trade_group:
        print("No open trade group found for symbol. Cannot add expired trade.")
        return

    # Create the expired trade entry
    trade = create_trade_entry(trade_data, trade_group.trade_group_id)
    session.add(trade)
    session.commit()

    print(f"Expired trade added with trade_id: {trade.trade_id} for group_id: {trade_group.trade_group_id}")
