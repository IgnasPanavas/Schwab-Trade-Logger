-- db_init/create_tables.sql

-- Create the Trades table
CREATE TABLE IF NOT EXISTS Trades (
    trade_id SERIAL PRIMARY KEY,
    trade_date DATE,
    action VARCHAR(20),
    symbol VARCHAR(10),
    description TEXT,
    contracts INT,
    price DECIMAL(10, 2),
    total_cost DECIMAL(10, 2),
    commission DECIMAL(10, 2),
    expiration_date DATE,
    strike_price DECIMAL(10, 2)
);

-- Create the Trade_Pairs table
CREATE TABLE IF NOT EXISTS Trade_Pairs (
    pair_id SERIAL PRIMARY KEY,
    open_trade_id INT REFERENCES Trades(trade_id),
    close_trade_id INT REFERENCES Trades(trade_id),
    open_date DATE,
    close_date DATE,
    contracts INT,
    pnl DECIMAL(10, 2)
);

-- Create the Positions table
CREATE TABLE IF NOT EXISTS Positions (
    position_id SERIAL PRIMARY KEY,
    open_trade_id INT REFERENCES Trades(trade_id),
    symbol VARCHAR(10),
    contracts INT,
    price DECIMAL(10, 2),
    total_cost DECIMAL(10, 2)
);
