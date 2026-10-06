import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS impacts (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS urgencies (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

cursor.executemany("""
    INSERT OR IGNORE INTO impacts (id, name)
    VALUES (?, ?)
""", [
    (1, "Low"),
    (2, "Medium"),
    (3, "High")
])

cursor.executemany("""
    INSERT OR IGNORE INTO urgencies (id, name)
    VALUES (?, ?)
""", [
    (1, "Low"),
    (2, "Medium"),
    (3, "High")
])

connection.commit()
connection.close()

print("Priority dimensions added successfully.")
