import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE ticket_escalations_new (
        id INTEGER PRIMARY KEY,
        ticket_id INTEGER NOT NULL,
        team_id INTEGER NOT NULL,
        reason TEXT NOT NULL,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        resolved_at TEXT,
        notes TEXT,
        UNIQUE(ticket_id, team_id, reason),
        FOREIGN KEY (ticket_id) REFERENCES tickets(id),
        FOREIGN KEY (team_id) REFERENCES teams(id)
    )
""")

cursor.execute("""
    INSERT INTO ticket_escalations_new
    (id, ticket_id, team_id, reason, created_at, resolved_at, notes)
    SELECT
        id,
        ticket_id,
        team_id,
        reason,
        created_at,
        resolved_at,
        notes
    FROM ticket_escalations
""")

cursor.execute("DROP TABLE ticket_escalations")

cursor.execute("""
    ALTER TABLE ticket_escalations_new
    RENAME TO ticket_escalations
""")

connection.commit()
connection.close()

print("Migration completed successfully.")