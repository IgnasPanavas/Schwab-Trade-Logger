from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Trade import Trade, Base  # Import your models
from models.TradeGroups import TradeGroup
from db_manager import get_db_session



# Function to add a trade
def add_trade(trade_data):
    with get_db_session() as session:
        # Check if this is an opening or closing trade
        if trade_data['action'] == 'buy':  # Assuming 'buy' is for opening trades
            # Create a new TradeGroup for opening trade
            trade_group = TradeGroup(
                symbol=trade_data['symbol'],
                total_quantity=trade_data['contracts'],
                open_quantity=trade_data['contracts'],  # All contracts are open initially
                status='open'  # Trade group is open
            )
            session.add(trade_group)
            session.commit()  # Commit to generate the trade_group_id

            # Now create the actual Trade entry
            trade = Trade(
                trade_group_id=trade_group.trade_group_id,
                trade_date=trade_data['trade_date'],
                action=trade_data['action'],
                symbol=trade_data['symbol'],
                description=trade_data.get('description'),
                contracts=trade_data['contracts'],
                price=trade_data['price'],
                total_cost=trade_data['total_cost'],
                commission=trade_data.get('commission'),
                expiration_date=trade_data.get('expiration_date'),
                strike_price=trade_data.get('strike_price')
            )
            session.add(trade)
            session.commit()

            print(f"Opening trade added with trade_id: {trade.trade_id} and group_id: {trade_group.trade_group_id}")

        elif trade_data['action'] == 'sell':  # Assuming 'sell' is for closing trades
            # Find the corresponding TradeGroup
            trade_group = session.query(TradeGroup).filter(
                TradeGroup.symbol == trade_data['symbol'],
                TradeGroup.status != 'closed'
            ).first()

            if not trade_group:
                print("No open trade group found for symbol. Cannot add closing trade.")
                return

            # Calculate the remaining open quantity
            if trade_group.open_quantity >= trade_data['contracts']:
                trade_group.open_quantity -= trade_data['contracts']

                # Update the status of the trade group
                trade_group.update_status()

                # Now add the closing trade
                trade = Trade(
                    trade_group_id=trade_group.trade_group_id,
                    trade_date=trade_data['trade_date'],
                    action=trade_data['action'],
                    symbol=trade_data['symbol'],
                    description=trade_data.get('description'),
                    contracts=trade_data['contracts'],
                    price=trade_data['price'],
                    total_cost=trade_data['total_cost'],
                    commission=trade_data.get('commission'),
                    expiration_date=trade_data.get('expiration_date'),
                    strike_price=trade_data.get('strike_price')
                )
                session.add(trade)
                session.commit()

                print(f"Closing trade added with trade_id: {trade.trade_id} for group_id: {trade_group.trade_group_id}")
            else:
                print("Error: Closing more contracts than open in the trade group.")

# Example of adding an opening trade
opening_trade_data = {
    'trade_date': '2024-10-12',
    'action': 'buy',
    'symbol': 'AAPL',
    'contracts': 100,
    'price': 150.00,
    'total_cost': 15000.00,
    'commission': 10.00,
    'expiration_date': None,
    'strike_price': None
}
add_trade(opening_trade_data)

# Example of adding a closing trade
closing_trade_data = {
    'trade_date': '2024-10-15',
    'action': 'sell',
    'symbol': 'AAPL',
    'contracts': 40,
    'price': 155.00,
    'total_cost': 6200.00,
    'commission': 10.00,
    'expiration_date': None,
    'strike_price': None
}
add_trade(closing_trade_data)
