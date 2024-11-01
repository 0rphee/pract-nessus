import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

# Create a table for storing names
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
''')

# Optionally, insert some sample data
sample_names = ["Alice", "Bob", "Charlie", "Diana"]
cursor.executemany("INSERT INTO users (name) VALUES (?)", [(name,) for name in sample_names])

conn.commit()
conn.close()
