from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, Enum
from models import Base
from sqlalchemy.orm import relationship
import enum


# Enum for trade status
class TradeStatus(enum.Enum):
    open = 'open'
    partially_closed = 'partially_closed'
    closed = 'closed'

class Trade(Base):
    __tablename__ = 'Trades'

    # Table fields
    trade_id = Column(Integer, primary_key=True, autoincrement=True)
    trade_group_id = Column(Integer, ForeignKey('TradeGroups.trade_group_id'), nullable=False)
    trade_date = Column(Date, nullable=False)
    action = Column(String(20), nullable=False)  # 'buy' or 'sell'
    symbol = Column(String(50), nullable=False)
    description = Column(String, nullable=True)
    contracts = Column(Integer, nullable=False)
    price = Column(DECIMAL(10, 2), nullable=False)
    total_cost = Column(DECIMAL(10, 2), nullable=False)
    commission = Column(DECIMAL(10, 2), nullable=True)
    expiration_date = Column(Date, nullable=True)
    strike_price = Column(DECIMAL(10, 2), nullable=True)

    # Relationships
    trade_group = relationship('TradeGroup', back_populates='trades')

    def __repr__(self):
        return f"<Trade(id={self.trade_id}, symbol={self.symbol}, action={self.action}, contracts={self.contracts})>"

    # Example conversion method from dictionary to model object
    @classmethod
    def from_dict(cls, data):
        return cls(
            trade_date=data.get('trade_date'),
            action=data.get('action'),
            symbol=data.get('symbol'),
            description=data.get('description'),
            contracts=data.get('contracts'),
            price=data.get('price'),
            total_cost=data.get('total_cost'),
            commission=data.get('commission'),
            expiration_date=data.get('expiration_date'),
            strike_price=data.get('strike_price')
        )

    # Example conversion method from model object to dictionary
    def to_dict(self):
        return {
            'trade_id': self.trade_id,
            'trade_group_id': self.trade_group_id,
            'trade_date': self.trade_date,
            'action': self.action,
            'symbol': self.symbol,
            'description': self.description,
            'contracts': self.contracts,
            'price': self.price,
            'total_cost': self.total_cost,
            'commission': self.commission,
            'expiration_date': self.expiration_date,
            'strike_price': self.strike_price
        }

