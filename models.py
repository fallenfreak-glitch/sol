import sqlite3

def init_db():
    conn = sqlite3.connect("trades.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS trades (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            token_address TEXT UNIQUE,
            deployer TEXT,
            funded_wallet TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def log_trade(token_address, deployer, funded_wallet):
    conn = sqlite3.connect("trades.db")
    c = conn.cursor()
    try:
        c.execute('''
            INSERT INTO trades (token_address, deployer, funded_wallet)
            VALUES (?, ?, ?)
        ''', (token_address, deployer, funded_wallet))
        conn.commit()
    except sqlite3.IntegrityError:
        pass
    finally:
        conn.close()
