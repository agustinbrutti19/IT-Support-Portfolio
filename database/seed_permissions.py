import sqlite3

DB_PATH = "database/database.db"

permissions = [
    "Login",
    "Read",
    "Create",
    "Edit",
    "Delete",
    "Admin"
]

connection = sqlite3.connect(DB_PATH)
cursor = connection.cursor()

for permission in permissions:
    cursor.execute(
        "INSERT OR IGNORE INTO permissions (name) VALUES (?)",
        (permission,)
    )

connection.commit()
connection.close()

print("Permissions inserted successfully.")