import sqlite3
from pathlib import Path

database_path = Path(__file__).parent / "database.db"

connection = sqlite3.connect(database_path)

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS departments (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

departments = [
    ("Reservations",),
    ("Concierge",),
    ("Sales",),
    ("Marketing",),
    ("Operations",),
    ("Administration",),
    ("IT",)
]

cursor.execute("""
    CREATE TABLE IF NOT EXISTS teams (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

teams = [
    ("Helpdesk",),
    ("Engineering",),
    ("Product",),
    ("Vendor Support",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO teams (name) VALUES (?)",
    teams
)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        department_id INTEGER NOT NULL,
        role TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'Active',
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        deactivated_at TEXT,
        FOREIGN KEY (department_id) REFERENCES departments(id)
    )
""")

cursor.executemany(
    "INSERT OR IGNORE INTO departments (name) VALUES (?)",
    departments
)

users = [
    ("Sarah Johnson", "sarah.johnson@borealistravel.com", 1, "Reservations Specialist"),
    ("Michael Brown", "michael.brown@borealistravel.com", 2, "Concierge Specialist"),
    ("Emily Davis", "emily.davis@borealistravel.com", 3, "Sales Representative"),
    ("Daniel Wilson", "daniel.wilson@borealistravel.com", 4, "Marketing Specialist"),
    ("Olivia Martinez", "olivia.martinez@borealistravel.com", 5, "Operations Coordinator"),
    ("James Taylor", "james.taylor@borealistravel.com", 6, "Administrative Assistant"),
    ("Alex Carter", "alex.carter@borealistravel.com", 7, "Helpdesk Technician")
]

cursor.executemany("""
    INSERT OR IGNORE INTO users
    (name, email, department_id, role)
    VALUES (?, ?, ?, ?)
""", users)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

categories = [
    ("Hardware",),
    ("Software",),
    ("Access / Permissions",),
    ("Network",),
    ("Microsoft 365",),
    ("Communication",),
    ("Account",),
    ("Other",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO categories (name) VALUES (?)",
    categories
)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS priorities (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

priorities = [
    ("Low",),
    ("Medium",),
    ("High",),
    ("Critical",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO priorities (name) VALUES (?)",
    priorities
)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS statuses (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL UNIQUE
    )
""")

statuses = [
    ("Open",),
    ("In Progress",),
    ("Pending",),
    ("Resolved",),
    ("Closed",)
]

cursor.executemany(
    "INSERT OR IGNORE INTO statuses (name) VALUES (?)",
    statuses
)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tickets (
        id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        description TEXT NOT NULL,
        category_id INTEGER NOT NULL,
        priority_id INTEGER NOT NULL,
        status_id INTEGER NOT NULL,
        assigned_to INTEGER,
        created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        updated_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
        resolved_at TEXT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (category_id) REFERENCES categories(id),
        FOREIGN KEY (priority_id) REFERENCES priorities(id),
        FOREIGN KEY (status_id) REFERENCES statuses(id),
        FOREIGN KEY (assigned_to) REFERENCES users(id)
    )
""")

ticket = (
    1,
    1,
    "CRM Access Denied",
    "Sarah Johnson is unable to access the CRM. The application displays an Access Denied message.",
    3,
    3,
    4,
    7
)

cursor.execute("""
    INSERT OR IGNORE INTO tickets
    (
        id,
        user_id,
        title,
        description,
        category_id,
        priority_id,
        status_id,
        assigned_to
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ticket)

ticket_2 = (
    2,
    1,
    "CRM error during reservation",
    "CRM displays an error when Sarah attempts to create a new reservation.",
    2,
    3,
    1,
    7
)

cursor.execute("""
    INSERT OR IGNORE INTO tickets
    (
        id,
        user_id,
        title,
        description,
        category_id,
        priority_id,
        status_id,
        assigned_to
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ticket_2)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ticket_updates (
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

updates = [
    (1, 7, "Ticket created and assigned to Helpdesk."),
    (1, 7, "Verified that Sarah's user account is active."),
    (1, 7, "Confirmed that Sarah's Microsoft 365 account is working correctly."),
    (1, 7, "Verified that Sarah was missing the required CRM access group."),
    (1, 7, "Added Sarah to the appropriate CRM access group."),
    (1, 7, "Asked Sarah to sign out and sign in again."),
    (1, 7, "Sarah confirmed that she was able to access the CRM successfully.")
]

cursor.executemany("""
    INSERT OR IGNORE INTO ticket_updates
    (ticket_id, user_id, note)
    VALUES (?, ?, ?)
""", updates)

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ticket_escalations (
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

escalation = (
    2,
    2,
    "CRM error reproducible"
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_escalations
    (
        ticket_id,
        team_id,
        reason
    )
    VALUES (?, ?, ?)
""", escalation)

update = (
    2,
    7,
    "Engineering identified a backend issue affecting reservation creation."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update)

cursor.execute("""
    UPDATE ticket_escalations
    SET
        resolved_at = CURRENT_TIMESTAMP,
        notes = 'Engineering identified and fixed a backend issue affecting reservation creation.'
    WHERE ticket_id = 2
      AND team_id = 2
      AND resolved_at IS NULL
""")

update_2 = (
    2,
    7,
    "Helpdesk tested the Engineering fix and confirmed that reservation creation works correctly."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_2)

update_3 = (
    2,
    1,
    "Sarah confirmed that the CRM is working correctly and reservation creation is successful."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_3)

cursor.execute("""
    UPDATE tickets
    SET
        status_id = 4,
        resolved_at = CURRENT_TIMESTAMP,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = 2
      AND status_id != 4
""")

ticket_3 = (
    3,
    3,
    "Microsoft 365 login problem",
    "Sarah Johnson is unable to sign in to Microsoft 365.",
    5,
    3,
    1,
    7
)

cursor.execute("""
    INSERT OR IGNORE INTO tickets
    (
        id,
        user_id,
        title,
        description,
        category_id,
        priority_id,
        status_id,
        assigned_to
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ticket_3)

update_4 = (
    3,
    7,
    "Ticket created and assigned to Helpdesk."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_4)

update_5 = (
    3,
    7,
    "Verified that Emily's Microsoft 365 account is active."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_5)

update_6 = (
    3,
    7,
    "Confirmed that Microsoft 365 services are available and other users can sign in normally."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_6)

update_7 = (
    3,
    7,
    "Reviewed the sign-in issue and identified that Emily's Microsoft 365 password has expired."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_7)

update_8 = (
    3,
    7,
    "Assisted Emily with resetting her Microsoft 365 password."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_8)

update_9 = (
    3,
    3,
    "Emily confirmed that she can successfully sign in to Microsoft 365."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_9)

cursor.execute("""
    UPDATE tickets
    SET
        status_id = 4,
        resolved_at = CURRENT_TIMESTAMP,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = 3
      AND status_id != 4
""")

ticket_4 = (
    4,
    2,
    "Zoom microphone not working",
    "Michael Brown reports that his microphone is not working during Zoom meetings.",
    6,
    2,
    1,
    7
)

cursor.execute("""
    INSERT OR IGNORE INTO tickets
    (
        id,
        user_id,
        title,
        description,
        category_id,
        priority_id,
        status_id,
        assigned_to
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ticket_4)

cursor.execute("""
    UPDATE tickets
    SET
        status_id = 2,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = 4
      AND status_id = 1
""")

update_10 = (
    4,
    7,
    "Started troubleshooting the Zoom microphone issue."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_10)

update_11 = (
    4,
    7,
    "Verified that Windows detects Michael's microphone correctly."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_11)

update_12 = (
    4,
    7,
    "Verified that Zoom was using the wrong microphone input device."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_12)

update_13 = (
    4,
    7,
    "Selected the correct microphone input device in Zoom."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_13)

update_14 = (
    4,
    2,
    "Michael tested the microphone in Zoom and confirmed that audio input is working correctly."
)

cursor.execute("""
    INSERT OR IGNORE INTO ticket_updates
    (
        ticket_id,
        user_id,
        note
    )
    VALUES (?, ?, ?)
""", update_14)

cursor.execute("""
    UPDATE tickets
    SET
        status_id = 4,
        resolved_at = CURRENT_TIMESTAMP,
        updated_at = CURRENT_TIMESTAMP
    WHERE id = 4
      AND status_id != 4
""")

connection.commit()
connection.close()