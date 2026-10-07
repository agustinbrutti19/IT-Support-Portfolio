import sqlite3

DB_PATH = "database/database.db"

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS group_permissions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    group_id INTEGER NOT NULL,
    system_id INTEGER NOT NULL,
    permission_id INTEGER NOT NULL,
    UNIQUE(group_id, system_id, permission_id),
    FOREIGN KEY (group_id) REFERENCES groups(id),
    FOREIGN KEY (system_id) REFERENCES systems(id),
    FOREIGN KEY (permission_id) REFERENCES permissions(id)
)
""")

connection.commit()
connection.close()

print("Group permissions table created successfully.")