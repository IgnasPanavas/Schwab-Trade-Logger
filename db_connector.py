from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

db_username = os.environ["DB_USERNAME"]
db_password = os.environ["DB_PASSWORD"]


DATABASE_URL = f"postgresql://{db_username}:{db_password}@localhost:5432/trades_db"
engine = create_engine(DATABASE_URL)

# Test connection
connection = engine.connect()
print("Connected to the database!")
connection.close()
