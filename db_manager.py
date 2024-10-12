from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.Trade import Base  # Import your base model
import os
from dotenv import load_dotenv
import psycopg2
from contextlib import contextmanager  # Import contextmanager

# Load environment variables from the .env file
load_dotenv()

# Fetch the necessary database credentials from environment variables
username = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")
db_host = os.getenv("DB_HOST", "localhost")  # Optional, defaults to localhost

# Step 1: Connect to the 'postgres' database to check if the target database exists
DATABASE_URL_DEFAULT = f'postgresql://{username}:{password}@{db_host}/postgres'

def create_database_if_not_exists(db_name):
    """
    Function to create the database if it doesn't exist.
    """
    # Connect to the default 'postgres' database
    try:
        conn = psycopg2.connect(DATABASE_URL_DEFAULT)
        conn.autocommit = True
        cursor = conn.cursor()
        cursor.execute(f"SELECT 1 FROM pg_database WHERE datname = '{db_name}';")
        exists = cursor.fetchone()
        if not exists:
            cursor.execute(f"CREATE DATABASE {db_name};")
            print(f"Database '{db_name}' created successfully.")
        else:
            print(f"Database '{db_name}' already exists.")
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error creating database: {e}")

# Call the function to ensure the database is created
create_database_if_not_exists(db_name)

# Step 2: Connect to the target database
DATABASE_URL = f'postgresql://{username}:{password}@{db_host}/{db_name}'
engine = create_engine(DATABASE_URL)

# Create the session maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Step 3: Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Step 4: Define the get_db_session() function as a context manager
@contextmanager
def get_db_session():
    """
    Context manager to get a new SQLAlchemy session.
    This ensures the session is closed after use.
    Usage:
        with get_db_session() as session:
            # your database queries
    """
    session = SessionLocal()
    try:
        yield session  # Provide the session to the calling code
        session.commit()  # Commit the session if everything goes well
    except Exception:
        session.rollback()  # Rollback in case of an exception
        raise  # Re-raise the exception after rollback
    finally:
        session.close()  # Always close the session to prevent connection leaks
