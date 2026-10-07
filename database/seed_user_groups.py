import sqlite3

DB_PATH = "database/database.db"

user_groups = [
    (1, "CRM-Reservations"),
    (1, "Microsoft365-Users"),
    (1, "Zoom-Users"),
    (1, "Front-Reservations"),
    (1, "SharedDrive-Reservations")
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for user_id, group_name in user_groups:
    cursor.execute(
        """
        INSERT OR IGNORE INTO user_groups (user_id, group_id)
        SELECT ?, groups.id
        FROM groups
        WHERE groups.name = ?
        """,
        (user_id, group_name)
    )

connection.commit()
connection.close()

print("User groups inserted successfully.")