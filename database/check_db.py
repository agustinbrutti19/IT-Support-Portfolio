import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    PRAGMA foreign_key_list(ticket_escalations)
""")

for row in cursor.fetchall():
    print(row)

connection.close()