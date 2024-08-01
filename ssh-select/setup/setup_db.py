import sqlite3

# Connect to SQLite database (it will create the database file if it does not exist)
def connect_db():
    return sqlite3.connect('data/hosts.db')

# Create tables for groups and hosts
def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Create tables
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS groups (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE
    )
    ''')

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hosts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        group_id INTEGER,
        alias TEXT,
        hostname TEXT,
        user TEXT,
        key_path TEXT,
        FOREIGN KEY (group_id) REFERENCES groups (id)
    )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_db()
    print("Database setup complete.")

