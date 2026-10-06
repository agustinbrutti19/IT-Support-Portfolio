import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    ALTER TABLE tickets
    ADD COLUMN impact_id INTEGER
""")

cursor.execute("""
    ALTER TABLE tickets
    ADD COLUMN urgency_id INTEGER
""")

connection.commit()
connection.close()

print("Ticket priority fields added successfully.")