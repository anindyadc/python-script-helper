# SSH Select Project

## Overview

This project provides a Python-based interface for selecting and connecting to remote servers via SSH. The servers and groups are managed using an SQLite database.

## Project Structure

- `data/`: Directory containing the SQLite database (`hosts.db`).
- `scripts/`:
  - `insert_data.py`: Script to insert initial data into the database.
  - `ssh_select.py`: Script to select a host and connect via SSH.
- `setup/`:
  - `setup_db.py`: Script to set up the SQLite database schema.

## Setup Instructions

1. **Set up the database schema:**

   ```bash
   python setup/setup_db.py

