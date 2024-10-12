from sqlalchemy.ext.declarative import declarative_base

# Create the declarative base shared across all models
Base = declarative_base()

# Import your models so they are registered with SQLAlchemy's metadata
from .Trade import Trade
from .TradeGroups import TradeGroup