import sqlite3
from pathlib import Path

database_path = Path(__file__).parent.parent / "database" / "database.db"


def get_connection():
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    return connection

def get_open_ticket_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(tickets.id)
        FROM tickets
        JOIN statuses
            ON tickets.status_id = statuses.id
        WHERE statuses.name IN ('Open', 'In Progress', 'Pending')
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]

def get_high_priority_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(tickets.id)
        FROM tickets
        JOIN priorities
            ON tickets.priority_id = priorities.id
        WHERE priorities.name = 'High'
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]

def get_resolved_ticket_count():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT COUNT(tickets.id)
        FROM tickets
        JOIN statuses
            ON tickets.status_id = statuses.id
        WHERE statuses.name = 'Resolved'
    """)

    result = cursor.fetchone()

    connection.close()

    return result[0]

def get_recent_tickets():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            tickets.id,
            tickets.title,
            users.name AS user_name,
            priorities.name AS priority,
            statuses.name AS status
        FROM tickets
        JOIN users
            ON tickets.user_id = users.id
        JOIN priorities
            ON tickets.priority_id = priorities.id
        JOIN statuses
            ON tickets.status_id = statuses.id
        ORDER BY tickets.id DESC
        LIMIT 5
    """)

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def create_ticket(title, description, user_id, category_id, priority_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO tickets
        (
            user_id,
            title,
            description,
            category_id,
            priority_id,
            status_id,
            assigned_to
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        title,
        description,
        category_id,
        priority_id,
        1,
        7
    ))

    connection.commit()

    ticket_id = cursor.lastrowid

    connection.close()

    return ticket_id

def get_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM users
        WHERE status = 'Active'
        ORDER BY name
    """)

    users = cursor.fetchall()

    connection.close()

    return users

def get_categories():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM categories
        ORDER BY name
    """)

    categories = cursor.fetchall()

    connection.close()

    return categories

def get_priorities():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM priorities
        ORDER BY id
    """)

    priorities = cursor.fetchall()

    connection.close()

    return priorities



