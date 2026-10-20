import os
import sqlite3
from pathlib import Path
from database.calculate_priority import calculate_priority

database_path = Path(
    os.getenv(
        "DATABASE_PATH",
        str(Path(__file__).parent.parent / "database" / "database.db")
    )
)

def get_connection():
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    connection.execute("PRAGMA foreign_keys = ON")
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
        JOIN statuses
            ON tickets.status_id = statuses.id
        WHERE priorities.name IN ('High', 'Critical')
          AND statuses.name NOT IN ('Resolved', 'Closed')
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

def get_all_tickets():
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
    """)

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def search_tickets(search_term):
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
        WHERE tickets.title LIKE ?
           OR tickets.description LIKE ?
           OR users.name LIKE ?
        ORDER BY tickets.id DESC
    """, (
        f"%{search_term}%",
        f"%{search_term}%",
        f"%{search_term}%"
    ))

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def get_tickets_by_status(status_id):
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
        WHERE tickets.status_id = ?
        ORDER BY tickets.id DESC
    """, (status_id,))

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def get_ticket_status_counts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            statuses.name AS status,
            COUNT(tickets.id) AS total
        FROM statuses
        LEFT JOIN tickets
            ON tickets.status_id = statuses.id
        GROUP BY statuses.id, statuses.name
        ORDER BY statuses.id
    """)

    results = cursor.fetchall()
    connection.close()

    return results

def get_tickets_by_priority(priority_id):
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
        WHERE tickets.priority_id = ?
        ORDER BY tickets.id DESC
    """, (priority_id,))

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def get_critical_open_tickets():
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
        WHERE priorities.name = 'Critical'
          AND statuses.name NOT IN ('Resolved', 'Closed')
        ORDER BY tickets.id DESC
    """)

    tickets = cursor.fetchall()
    connection.close()

    return tickets

def create_ticket_creation_update(ticket_id, user_id, priority):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO ticket_updates
        (ticket_id, user_id, note)
        VALUES (?, ?, ?)
    """, (
        ticket_id,
        user_id,
        f"Ticket created with {priority} priority."
    ))

    connection.commit()
    connection.close()

def create_ticket(
    title,
    description,
    user_id,
    category_id,
    impact_id,
    urgency_id
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM impacts
        WHERE id = ?
    """, (impact_id,))

    impact = cursor.fetchone()[0]

    cursor.execute("""
        SELECT name
        FROM urgencies
        WHERE id = ?
    """, (urgency_id,))

    urgency = cursor.fetchone()[0]

    priority_name = calculate_priority(impact, urgency)

    priority_id = get_priority_id(priority_name)

    cursor.execute("""
        INSERT INTO tickets
        (
            user_id,
            title,
            description,
            category_id,
            priority_id,
            impact_id,
            urgency_id,
            status_id,
            assigned_to
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        title,
        description,
        category_id,
        priority_id,
        impact_id,
        urgency_id,
        1,
        7
    ))

    connection.commit()

    ticket_id = cursor.lastrowid

    create_ticket_creation_update(
        ticket_id,
        7,
        priority_name
    )

    connection.close()

    return ticket_id

def update_ticket(ticket_id, title, description, category_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tickets
        SET title = ?,
            description = ?,
            category_id = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (
        title,
        description,
        category_id,
        ticket_id
    ))

    connection.commit()
    connection.close()

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

def get_all_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            users.id,
            users.name,
            users.email,
            users.role,
            users.status,
            departments.name AS department
        FROM users
        LEFT JOIN departments
            ON users.department_id = departments.id
        ORDER BY users.name
    """)

    users = cursor.fetchall()

    connection.close()

    return users

def get_user_by_id(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            users.id,
            users.name,
            users.email,
            users.role,
            users.status,
            users.created_at,
            users.deactivated_at,
            departments.name AS department
        FROM users
        LEFT JOIN departments
            ON users.department_id = departments.id
        WHERE users.id = ?
    """, (user_id,))

    user = cursor.fetchone()

    connection.close()

    return user

def get_user_groups(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            groups.id,
            groups.name
        FROM user_groups
        INNER JOIN groups
            ON user_groups.group_id = groups.id
        WHERE user_groups.user_id = ?
        ORDER BY groups.name
    """, (user_id,))

    groups = cursor.fetchall()

    connection.close()

    return groups

def get_user_access(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            groups.name AS group_name,
            systems.name AS system_name,
            GROUP_CONCAT(
                permissions.name,
                ', '
            ) AS permissions
        FROM user_groups
        INNER JOIN groups
            ON user_groups.group_id = groups.id
        INNER JOIN group_permissions
            ON groups.id = group_permissions.group_id
        INNER JOIN systems
            ON group_permissions.system_id = systems.id
        INNER JOIN permissions
            ON group_permissions.permission_id = permissions.id
        WHERE user_groups.user_id = ?
        GROUP BY groups.id, systems.id
        ORDER BY groups.name, systems.name
    """, (user_id,))

    access = cursor.fetchall()

    connection.close()

    return access

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

def get_ticket(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            tickets.id,
            tickets.title,
            tickets.description,
            tickets.category_id,
            users.name AS user_name,
            assigned_user.name AS assigned_to_name,
            priorities.name AS priority,
            statuses.name AS status,
            categories.name AS category,
            impacts.name AS impact,
            urgencies.name AS urgency
        FROM tickets
        JOIN users
            ON tickets.user_id = users.id
        LEFT JOIN users AS assigned_user
            ON tickets.assigned_to = assigned_user.id
        JOIN priorities
            ON tickets.priority_id = priorities.id
        JOIN statuses
            ON tickets.status_id = statuses.id
        JOIN categories
            ON tickets.category_id = categories.id
        LEFT JOIN impacts
            ON tickets.impact_id = impacts.id
        LEFT JOIN urgencies
            ON tickets.urgency_id = urgencies.id
        WHERE tickets.id = ?
    """, (ticket_id,))

    ticket = cursor.fetchone()

    connection.close()

    return ticket

def get_ticket_updates(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            ticket_updates.id,
            ticket_updates.note,
            ticket_updates.created_at,
            users.name AS user_name
        FROM ticket_updates
        JOIN users
            ON ticket_updates.user_id = users.id
        WHERE ticket_updates.ticket_id = ?
        ORDER BY ticket_updates.created_at ASC, ticket_updates.id ASC
    """, (ticket_id,))

    updates = cursor.fetchall()

    connection.close()

    return updates

def get_ticket_escalations(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            ticket_escalations.id,
            teams.name AS team_name,
            ticket_escalations.reason,
            ticket_escalations.created_at,
            ticket_escalations.resolved_at,
            ticket_escalations.notes
        FROM ticket_escalations
        JOIN teams
            ON ticket_escalations.team_id = teams.id
        WHERE ticket_escalations.ticket_id = ?
        ORDER BY ticket_escalations.created_at ASC
    """, (ticket_id,))

    escalations = cursor.fetchall()

    connection.close()

    return escalations

def create_ticket_update(ticket_id, user_id, note):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO ticket_updates
            (ticket_id, user_id, note)
            VALUES (?, ?, ?)
        """, (
            ticket_id,
            user_id,
            note
        ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_statuses():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM statuses
        ORDER BY id
    """)

    statuses = cursor.fetchall()

    connection.close()

    return statuses

def update_ticket_status(ticket_id, status_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tickets
        SET status_id = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (
        status_id,
        ticket_id
    ))

    connection.commit()

    connection.close()

def get_ticket_status(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT statuses.name
        FROM tickets
        JOIN statuses
            ON tickets.status_id = statuses.id
        WHERE tickets.id = ?
    """, (ticket_id,))

    result = cursor.fetchone()

    connection.close()

    return result[0] if result else None

def get_status_name(status_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT name
        FROM statuses
        WHERE id = ?
    """, (status_id,))

    result = cursor.fetchone()

    connection.close()

    return result[0] if result else None

def get_it_users():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            users.id,
            users.name
        FROM users
        JOIN departments
            ON users.department_id = departments.id
        WHERE departments.name = 'IT'
          AND users.status = 'Active'
        ORDER BY users.name
    """)

    users = cursor.fetchall()

    connection.close()

    return users

def update_ticket_assignment(ticket_id, user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE tickets
        SET assigned_to = ?,
            updated_at = CURRENT_TIMESTAMP
        WHERE id = ?
    """, (
        user_id,
        ticket_id
    ))

    connection.commit()
    connection.close()

def get_ticket_assigned_user(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            users.id,
            users.name
        FROM tickets
        JOIN users
            ON tickets.assigned_to = users.id
        WHERE tickets.id = ?
    """, (ticket_id,))

    user = cursor.fetchone()

    connection.close()

    return user

def is_valid_it_user(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT users.id
        FROM users
        JOIN departments
            ON users.department_id = departments.id
        WHERE users.id = ?
          AND departments.name = 'IT'
          AND users.status = 'Active'
    """, (user_id,))

    user = cursor.fetchone()

    connection.close()

    return user is not None

def get_priority_id(priority_name):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id
        FROM priorities
        WHERE name = ?
    """, (priority_name,))

    result = cursor.fetchone()

    connection.close()

    return result[0] if result else None

def get_impacts():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM impacts
        ORDER BY id
    """)

    impacts = cursor.fetchall()

    connection.close()

    return impacts

def get_urgencies():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM urgencies
        ORDER BY id
    """)

    urgencies = cursor.fetchall()

    connection.close()

    return urgencies

def get_filtered_tickets(
    search="",
    status_id=None,
    priority_id=None,
    assigned_to=None,
    category_id=None,
    sort="newest",
    limit=10,
    offset=0
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT
            tickets.id,
            tickets.title,
            users.name AS user_name,
            assigned_user.name AS assigned_to,
            categories.name AS category,
            priorities.name AS priority,
            statuses.name AS status
        FROM tickets
        JOIN users
            ON tickets.user_id = users.id
        LEFT JOIN users AS assigned_user
            ON tickets.assigned_to = assigned_user.id
        JOIN priorities
            ON tickets.priority_id = priorities.id
        JOIN statuses
            ON tickets.status_id = statuses.id
        JOIN categories
            ON tickets.category_id = categories.id
        WHERE 1=1
    """

    parameters = []

    if search:
        query += """
            AND (
                tickets.title LIKE ?
                OR tickets.description LIKE ?
                OR users.name LIKE ?
            )
        """

        search_value = f"%{search}%"

        parameters.extend([
            search_value,
            search_value,
            search_value
        ])

    if status_id is not None:
        query += " AND tickets.status_id = ?"
        parameters.append(status_id)

    if priority_id is not None:
        query += " AND tickets.priority_id = ?"
        parameters.append(priority_id)

    if assigned_to is not None:
        query += " AND tickets.assigned_to = ?"
        parameters.append(assigned_to)

    if category_id is not None:
        query += " AND tickets.category_id = ?"
        parameters.append(category_id)

    if sort == "oldest":
        query += " ORDER BY tickets.id ASC"
    elif sort == "priority":
        query += """
            ORDER BY tickets.priority_id DESC,
                    tickets.id DESC
        """
    else:
        query += " ORDER BY tickets.id DESC"
    
    query += " LIMIT ? OFFSET ?"
    parameters.extend([limit, offset])

    cursor.execute(query, parameters)

    tickets = cursor.fetchall()

    connection.close()

    return tickets

def count_filtered_tickets(
    search="",
    status_id=None,
    priority_id=None,
    assigned_to=None,
    category_id=None
):
    connection = get_connection()
    cursor = connection.cursor()

    query = """
        SELECT COUNT(tickets.id)
        FROM tickets
        JOIN users
            ON tickets.user_id = users.id
        WHERE 1=1
    """

    parameters = []

    if search:
        query += """
            AND (
                tickets.title LIKE ?
                OR tickets.description LIKE ?
                OR users.name LIKE ?
            )
        """

        search_value = f"%{search}%"

        parameters.extend([
            search_value,
            search_value,
            search_value
        ])

    if status_id is not None:
        query += " AND tickets.status_id = ?"
        parameters.append(status_id)

    if priority_id is not None:
        query += " AND tickets.priority_id = ?"
        parameters.append(priority_id)

    if assigned_to is not None:
        query += " AND tickets.assigned_to = ?"
        parameters.append(assigned_to)

    if category_id is not None:
        query += " AND tickets.category_id = ?"
        parameters.append(category_id)

    cursor.execute(query, parameters)

    total = cursor.fetchone()[0]

    connection.close()

    return total

def has_active_escalation(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT 1
        FROM ticket_escalations
        WHERE ticket_id = ?
          AND resolved_at IS NULL
        LIMIT 1
    """, (ticket_id,))

    result = cursor.fetchone()

    connection.close()

    return result is not None

def get_active_escalation(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            ticket_escalations.id,
            teams.name AS team,
            ticket_escalations.reason,
            ticket_escalations.created_at
        FROM ticket_escalations
        JOIN teams
            ON ticket_escalations.team_id = teams.id
        WHERE ticket_escalations.ticket_id = ?
          AND ticket_escalations.resolved_at IS NULL
        ORDER BY ticket_escalations.id DESC
        LIMIT 1
    """, (ticket_id,))

    escalation = cursor.fetchone()

    connection.close()

    return escalation

def create_ticket_escalation(ticket_id, team_id, reason):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO ticket_escalations (
            ticket_id,
            team_id,
            reason
        )
        VALUES (?, ?, ?)
    """, (
        ticket_id,
        team_id,
        reason
    ))

    connection.commit()
    connection.close()

def resolve_ticket_escalation(ticket_id, notes):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE ticket_escalations
        SET
            resolved_at = CURRENT_TIMESTAMP,
            notes = ?
        WHERE ticket_id = ?
          AND resolved_at IS NULL
    """, (
        notes,
        ticket_id
    ))

    connection.commit()
    connection.close()

def get_escalation_teams():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name
        FROM teams
        ORDER BY name
    """)

    teams = cursor.fetchall()

    connection.close()

    return teams

def get_bug_reports(ticket_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            bug_reports.id,
            bug_reports.ticket_id,
            bug_reports.title,
            bug_reports.description,
            bug_reports.steps_to_reproduce,
            bug_reports.expected_result,
            bug_reports.actual_result,
            impacts.name AS impact,
            bug_reports.environment,
            bug_reports.created_at
        FROM bug_reports
        JOIN impacts
            ON bug_reports.impact_id = impacts.id
        WHERE bug_reports.ticket_id = ?
        ORDER BY bug_reports.id DESC
    """, (ticket_id,))

    bug_reports = cursor.fetchall()

    connection.close()

    return bug_reports

def create_bug_report(
    ticket_id,
    title,
    description,
    steps_to_reproduce,
    expected_result,
    actual_result,
    impact_id,
    environment
):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO bug_reports (
            ticket_id,
            title,
            description,
            steps_to_reproduce,
            expected_result,
            actual_result,
            impact_id,
            environment
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        ticket_id,
        title,
        description,
        steps_to_reproduce,
        expected_result,
        actual_result,
        impact_id,
        environment
    ))

    connection.commit()

    bug_report_id = cursor.lastrowid

    connection.close()

    return bug_report_id

def get_all_groups():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, name
        FROM groups
        ORDER BY name
    """)

    groups = cursor.fetchall()

    connection.close()

    return groups

def update_user_groups(user_id, group_ids, change_reason):
    connection = get_connection()
    cursor = connection.cursor()

    # Get the user's current access groups
    cursor.execute(
        "SELECT group_id FROM user_groups WHERE user_id = ?",
        (user_id,)
    )
    current_group_ids = {
        row["group_id"] for row in cursor.fetchall()
    }

    # Normalize the submitted group IDs
    new_group_ids = set(group_ids)

    # Identify actual changes
    added_group_ids = new_group_ids - current_group_ids
    removed_group_ids = current_group_ids - new_group_ids

    try:
        # Replace the user's group assignments
        cursor.execute(
            "DELETE FROM user_groups WHERE user_id = ?",
            (user_id,)
        )

        for group_id in new_group_ids:
            cursor.execute("""
                INSERT INTO user_groups (user_id, group_id)
                VALUES (?, ?)
            """, (user_id, group_id))

        # Record groups that were added
        for group_id in added_group_ids:
            cursor.execute("""
                INSERT INTO access_audit_logs (
                    affected_user_id,
                    group_id,
                    action,
                    performed_by,
                    reason
                )
                VALUES (?, ?, 'ADDED', ?, ?)
            """, (
                user_id,
                group_id,
                "Alex Carter (IT Support)",
                change_reason
            ))

        # Record groups that were removed
        for group_id in removed_group_ids:
            cursor.execute("""
                INSERT INTO access_audit_logs (
                    affected_user_id,
                    group_id,
                    action,
                    performed_by,
                    reason
                )
                VALUES (?, ?, 'REMOVED', ?, ?)
            """, (
                user_id,
                group_id,
                "Alex Carter (IT Support)",
                change_reason
            ))

        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()

def get_access_audit_logs(user_id):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            access_audit_logs.id,
            groups.name AS group_name,
            access_audit_logs.action,
            access_audit_logs.performed_by,
            access_audit_logs.reason,
            access_audit_logs.created_at
        FROM access_audit_logs
        JOIN groups
            ON groups.id = access_audit_logs.group_id
        WHERE access_audit_logs.affected_user_id = ?
        ORDER BY access_audit_logs.id DESC
    """, (user_id,))

    logs = cursor.fetchall()
    connection.close()

    return logs

def get_all_access_audit_logs(
    user_name=None,
    action=None,
    start_date=None,
    end_date=None
):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        query = """
            SELECT
                access_audit_logs.id,
                users.name AS user_name,
                groups.name AS group_name,
                access_audit_logs.action,
                access_audit_logs.performed_by,
                access_audit_logs.reason,
                access_audit_logs.created_at
            FROM access_audit_logs
            JOIN users
                ON access_audit_logs.affected_user_id = users.id
            JOIN groups
                ON access_audit_logs.group_id = groups.id
            WHERE (? IS NULL OR users.name LIKE ?)
              AND (? IS NULL OR access_audit_logs.action = ?)
              AND (? IS NULL OR date(access_audit_logs.created_at) >= date(?))
              AND (? IS NULL OR date(access_audit_logs.created_at) <= date(?))
            ORDER BY access_audit_logs.id DESC
        """

        search_value = f"%{user_name}%" if user_name else None

        cursor.execute(
            query,
            (
                user_name,
                search_value,
                action,
                action,
                start_date,
                start_date,
                end_date,
                end_date
            )
        )

        return cursor.fetchall()

    finally:
        connection.close()
