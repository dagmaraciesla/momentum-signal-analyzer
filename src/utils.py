## data pipeline 
import sqlite3
import pandas as pd
import yfinance as yf


def initialize_db(db_path: str = "momentum.db") -> None:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS prices (
            ticker    TEXT NOT NULL, 
            date      TEXT NOT NULL,
            adj_close FLOAT NOT NULL,
            PRIMARY KEY (ticker, date)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS signals (
            ticker    TEXT NOT NULL, 
            ranking_date TEXT NOT NULL,
            momentum_score FLOAT,
            decile INTEGER,   
            PRIMARY KEY (ticker, ranking_date)
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS forward_returns (
            ticker    TEXT NOT NULL, 
            ranking_date TEXT NOT NULL,
            horizon_months INTEGER NOT NULL,
            return_pct FLOAT,
            PRIMARY KEY (ticker, ranking_date, horizon_months)
        )
    """)

    conn.commit()
    conn.close()


def fetch_prices(tickers: list[str], start: str, end: str) -> pd.DataFrame:
    df = yf.download(tickers, start=start, end=end, auto_adjust=True, progress=False)
    return df["Close"]
    

def clean_prices():
    pass

def compute_momentum_score():
    pass

def assign_deciles():
    pass

def compute_signals():
    pass

def compute_forward_returns():
    pass

def save_prices():
    pass

