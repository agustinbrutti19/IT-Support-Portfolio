import sqlite3

DB_PATH = "database/database.db"

group_permissions = [
    ("CRM-Reservations", "CRM", "Login"),
    ("CRM-Reservations", "CRM", "Read"),
    ("CRM-Reservations", "CRM", "Create"),
    ("CRM-Reservations", "CRM", "Edit"),

    ("Microsoft365-Users", "Microsoft 365", "Login"),
    ("Microsoft365-Users", "Microsoft 365", "Read"),
    ("Microsoft365-Users", "Microsoft 365", "Create"),
    ("Microsoft365-Users", "Microsoft 365", "Edit"),

    ("Zoom-Users", "Zoom", "Login"),
    ("Zoom-Users", "Zoom", "Read"),
    ("Zoom-Users", "Zoom", "Create"),
    ("Zoom-Users", "Zoom", "Edit"),

    ("Front-Reservations", "Front", "Login"),
    ("Front-Reservations", "Front", "Read"),
    ("Front-Reservations", "Front", "Create"),
    ("Front-Reservations", "Front", "Edit"),

    ("SharedDrive-Reservations", "Shared Drives", "Login"),
    ("SharedDrive-Reservations", "Shared Drives", "Read"),
    ("SharedDrive-Reservations", "Shared Drives", "Create"),
    ("SharedDrive-Reservations", "Shared Drives", "Edit")
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for group_name, system_name, permission_name in group_permissions:
    cursor.execute(
        """
        INSERT OR IGNORE INTO group_permissions
        (group_id, system_id, permission_id)
        SELECT groups.id, systems.id, permissions.id
        FROM groups, systems, permissions
        WHERE groups.name = ?
          AND systems.name = ?
          AND permissions.name = ?
        """,
        (group_name, system_name, permission_name)
    )

connection.commit()
connection.close()

print("Group permissions inserted successfully.")