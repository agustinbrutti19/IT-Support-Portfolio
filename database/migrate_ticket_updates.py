import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE ticket_updates_new (
        id INTEGER PRIMARY KEY,
        ticket_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        note TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        UNIQUE(ticket_id, user_id, note),
        FOREIGN KEY (ticket_id) REFERENCES tickets(id),
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
""")

cursor.execute("""
    INSERT INTO ticket_updates_new
    (id, ticket_id, user_id, note, created_at)
    SELECT id, ticket_id, user_id, note, created_at
    FROM ticket_updates
""")

cursor.execute("DROP TABLE ticket_updates")

cursor.execute("""
    ALTER TABLE ticket_updates_new
    RENAME TO ticket_updates
""")

connection.commit()
connection.close()

print("Migration completed successfully.")