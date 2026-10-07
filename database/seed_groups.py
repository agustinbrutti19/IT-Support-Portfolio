import sqlite3

DB_PATH = "database/database.db"

groups = [
    "CRM-Reservations",
    "Microsoft365-Users",
    "Zoom-Users",
    "Front-Reservations",
    "SharedDrive-Reservations"
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for group in groups:
    cursor.execute(
        "INSERT OR IGNORE INTO groups (name) VALUES (?)",
        (group,)
    )

connection.commit()
connection.close()

print("Groups inserted successfully.")