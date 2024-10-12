from sqlalchemy import Column, Integer, String, Date, DECIMAL, ForeignKey, Enum
from models import Base
from sqlalchemy.orm import relationship
import enum

# Enum for trade status
class TradeStatus(enum.Enum):
    open = 'open'
    partially_closed = 'partially_closed'
    closed = 'closed'

class TradeGroup(Base):
    __tablename__ = 'TradeGroups'

    trade_group_id = Column(Integer, primary_key=True, autoincrement=True)
    symbol = Column(String(10), nullable=False)
    total_quantity = Column(Integer, nullable=False)
    open_quantity = Column(Integer, nullable=False)
    status = Column(Enum(TradeStatus), default=TradeStatus.open, nullable=False)

    # Relationships
    trades = relationship('Trade', back_populates='trade_group')

    def __repr__(self):
        return f"<TradeGroup(id={self.trade_group_id}, symbol={self.symbol}, status={self.status})>"

    def update_status(self):
        if self.open_quantity == 0:
            self.status = TradeStatus.closed
        elif self.open_quantity < self.total_quantity:
            self.status = TradeStatus.partially_closed
        else:
            self.status = TradeStatus.open
