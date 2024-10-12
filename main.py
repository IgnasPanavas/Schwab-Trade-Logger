from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Trade import Trade, TradeGroup, Base  # Import your models
import os
from dotenv import load_dotenv
