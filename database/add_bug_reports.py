import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS bug_reports (
        id INTEGER PRIMARY KEY,
        ticket_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        steps_to_reproduce TEXT NOT NULL,
        expected_result TEXT NOT NULL,
        actual_result TEXT NOT NULL,
        impact_id INTEGER NOT NULL,
        environment TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (ticket_id) REFERENCES tickets(id),
        FOREIGN KEY (impact_id) REFERENCES impacts(id)
    )
""")

connection.commit()
connection.close()

print("Bug reports table created successfully.")