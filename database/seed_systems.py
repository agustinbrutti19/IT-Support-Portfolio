import sqlite3

DB_PATH = "database/database.db"

systems = [
    "Microsoft 365",
    "CRM",
    "Front",
    "Zoom",
    "Company Portal",
    "Shared Drives"
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for system in systems:
    cursor.execute(
        "INSERT OR IGNORE INTO systems (name) VALUES (?)",
        (system,)
    )

connection.commit()
connection.close()

print("Systems inserted successfully.")