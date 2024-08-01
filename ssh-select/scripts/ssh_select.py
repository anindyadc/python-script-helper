#!/usr/bin/env python3
import sqlite3
import subprocess

# Connect to SQLite database
def connect_db():
    return sqlite3.connect('data/hosts.db')

# List unique groups with sequential numbers
def list_groups():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, name FROM groups')
    groups = cursor.fetchall()
    conn.close()
    return groups

# List hosts within a selected group with sequential numbers
def list_hosts(group_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT id, alias FROM hosts WHERE group_id = ?', (group_id,))
    hosts = cursor.fetchall()
    conn.close()
    return hosts

# Get host details
def get_host_details(host_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        SELECT alias, hostname, user, key_path FROM hosts WHERE id = ?
    ''', (host_id,))
    details = cursor.fetchone()
    conn.close()
    return details

# Main function
def main():
    # List groups
    groups = list_groups()
    print("Select a group:")
    for index, (group_id, name) in enumerate(groups, start=1):
        print(f"{index}: {name}")

    group_choice = int(input("Enter the number of your choice: "))
    group_id = groups[group_choice - 1][0]

    # List hosts in the selected group
    hosts = list_hosts(group_id)
    print(f"Select a host in group '{groups[group_choice - 1][1]}':")
    for index, (host_id, alias) in enumerate(hosts, start=1):
        print(f"{index}: {alias}")

    host_choice = int(input("Enter the number of your choice: "))
    host_id = hosts[host_choice - 1][0]

    # Get host details
    details = get_host_details(host_id)
    if not details:
        print("Failed to get host details. Exiting.")
        return

    alias, hostname, user, key_path = details

    # Check if key exists
    if not subprocess.run(['test', '-f', key_path]).returncode == 0:
        print(f"RSA key file does not exist: {key_path}")
        return

    # Connect to the selected host
    print(f"Connecting to {hostname} as {user} using key {key_path}...")
    subprocess.run(['ssh', '-i', key_path, f'{user}@{hostname}'])

if __name__ == "__main__":
    main()

