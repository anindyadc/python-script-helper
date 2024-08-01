import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('data/hosts.db')

# Update RSA key path for a specific host
def update_key_path(host_alias, new_key_path):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Update the key_path for the host with the given alias
    cursor.execute('''
        UPDATE hosts
        SET key_path = ?
        WHERE alias = ?
    ''', (new_key_path, host_alias))
    
    if cursor.rowcount > 0:
        conn.commit()
        print(f"RSA key path for host '{host_alias}' updated successfully.")
    else:
        print(f"Host with alias '{host_alias}' not found.")
    
    conn.close()

# Example usage
def main():
    host_alias = input("Enter the alias of the host you want to update: ")
    new_key_path = input("Enter the new RSA key path: ")
    update_key_path(host_alias, new_key_path)

if __name__ == "__main__":
    main()

