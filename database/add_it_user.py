import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)
cursor = connection.cursor()

cursor.execute("""
    INSERT INTO users
    (name, email, department_id, role, status)
    VALUES (?, ?, ?, ?, ?)
""", (
    "Michael Smith",
    "michael.smith@borealistravel.com",
    7,
    "Helpdesk Technician",
    "Active"
))

connection.commit()
connection.close()

print("IT user added successfully.")
