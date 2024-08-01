import sqlite3

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('data/hosts.db')

# Insert a new group into the groups table
def insert_group(name):
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute('INSERT INTO groups (name) VALUES (?)', (name,))
        conn.commit()
        print(f"Group '{name}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Group '{name}' already exists.")
    finally:
        conn.close()

# Insert a new host into the hosts table
def insert_host(group_name, alias, hostname, user, key_path):
    conn = connect_db()
    cursor = conn.cursor()
    
    # Get the group ID
    cursor.execute('SELECT id FROM groups WHERE name = ?', (group_name,))
    group_id = cursor.fetchone()
    
    if group_id:
        group_id = group_id[0]
    else:
        print(f"Group '{group_name}' does not exist.")
        conn.close()
        return

    # Insert the host
    try:
        cursor.execute('''
            INSERT INTO hosts (group_id, alias, hostname, user, key_path)
            VALUES (?, ?, ?, ?, ?)
        ''', (group_id, alias, hostname, user, key_path))
        conn.commit()
        print(f"Host '{alias}' added successfully.")
    except sqlite3.IntegrityError:
        print(f"Host '{alias}' already exists.")
    finally:
        conn.close()

# Example usage
def main():
    # Insert groups
    insert_group('Mashmari')
    insert_group('AWS')
    
    # Insert hosts
    insert_host('Mashmari', 'Mashmari_VPN', '20.219.11.127', 'azureuser', '~/.ssh/id_rsa')
    insert_host('Mashmari', 'Mashmari_Megh', '20.219.61.15', 'azureuser', '~/.ssh/id_rsa')
    insert_host('AWS', 'TEST', 'AWS_TEST', 'AWS', '~/.ssh/id_rsa')

if __name__ == "__main__":
    main()

