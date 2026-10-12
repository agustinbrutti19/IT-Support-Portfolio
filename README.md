# IT Support & Helpdesk Lab

A practical IT Support and Helpdesk portfolio project built with Python, FastAPI, SQLite, and Jinja2.

This project simulates an internal IT environment for **Borealis Travel**, a fictional premium travel company. It demonstrates common IT support workflows, ticket management, user administration, access control, troubleshooting documentation, and audit logging.

## Project Objectives

- Simulate day-to-day internal IT support operations.
- Manage helpdesk tickets and their lifecycle.
- Organize ticket priorities based on impact and urgency.
- Manage users, departments, and access groups.
- Track ticket updates and escalations.
- Document software bugs and troubleshooting solutions.
- Maintain an audit trail of access group changes.

## Features

### 1. Dashboard

- Centralized overview of the helpdesk environment.
- Quick access to the main application sections.

### 2. Ticket Management

- Create and view support tickets.
- Categorize tickets by issue type.
- Assign priorities based on impact and urgency.
- Track ticket statuses throughout their lifecycle.
- Assign tickets to IT technicians.
- View ticket details and update history.

### 3. Ticket Escalation

- Escalate tickets to specialized teams.
- Record escalation details and notes.
- Track the progression of issues requiring additional technical support.

### 4. User Management

- View the user directory.
- Access individual user profiles.
- Associate users with departments.
- Review assigned access groups and available access information.

### 5. Access Group Management

- View access groups assigned to each user.
- Edit group assignments through the user profile.
- Validate submitted group IDs before updating assignments.
- Track changes to user access group memberships.

### 6. Access Group Audit Logging

The application records changes to user access group assignments.

- Records `ADDED` events when groups are assigned.
- Records `REMOVED` events when groups are removed.
- Identifies the affected user and access group.
- Stores the recorded technician identity.
- Records the date and time of each event.
- Displays audit history on the user's profile.
- Uses visual labels to distinguish additions and removals.
- Avoids creating audit entries when group assignments remain unchanged.

Audit events are stored in the SQLite `access_audit_logs` table.

**Current limitation:** The technician identity is simulated as `Alex Carter (IT Support)`. Authentication and automatic identification of the actual signed-in technician have not been implemented.

### 7. Bug Reporting

- Record software bug reports.
- Document reproduction steps.
- Describe expected and actual results.
- Associate reports with the relevant ticket workflow.

### 8. Knowledge Base

Includes knowledge base articles KB-001 through KB-005 to document troubleshooting guidance and common support procedures.

## Technology Stack

- **Python** — application logic
- **FastAPI** — web framework and routing
- **SQLite** — relational database
- **Jinja2** — HTML templating
- **HTML and CSS** — user interface
- **Git and GitHub** — version control and project hosting

## Project Structure

```text
IT-Support-Portfolio/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── knowledge_base.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── tickets.html
│   │   ├── new_ticket.html
│   │   ├── edit_ticket.html
│   │   ├── ticket_detail.html
│   │   ├── users.html
│   │   ├── user_detail.html
│   │   ├── knowledge_base.html
│   │   └── knowledge_base_article.html
│   └── static/
│       └── style.css
├── database/
│   ├── database.db
│   ├── init_db.py
│   ├── add_bug_reports.py
│   ├── add_groups_table.py
│   ├── add_group_permissions_table.py
│   ├── add_permissions_table.py
│   ├── add_systems_table.py
│   ├── add_user_groups_table.py
│   ├── seed_groups.py
│   ├── seed_permissions.py
│   ├── seed_systems.py
│   └── ...
├── docs/
│   ├── company.md
│   ├── users.md
│   ├── user-access-management.md
│   ├── tickets/
│   │   └── ticket-001.md
│   └── knowledge-base/
│       ├── README.md
│       ├── KB-001-crm-error-saving-customer-profile.md
│       ├── KB-002-microsoft-365-login-issues.md
│       ├── KB-003-zoom-microphone-troubleshooting.md
│       ├── KB-004-shared-drive-access-issues.md
│       └── KB-005-laptop-performance-troubleshooting.md
├── requirements.txt
└── README.md
```

## Running the Application

The project is developed locally with Python and a virtual environment.

### Prerequisites

- Python 3.13 or compatible version
- Git

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/agustinbrutti19/IT-Support-Portfolio.git
   cd IT-Support-Portfolio
   ```

2. Create a virtual environment:

   ```bash
   python -m venv .venv
   ```

3. Activate the environment.

   **Windows PowerShell:**

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

4. Install the application dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the development server:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Open the application in your browser:

   http://127.0.0.1:8000

**Database note:** The application uses `database/database.db`. Database initialization scripts should only be run when appropriate for the current database state, because reinitialization may affect existing data.

## Testing and Validation

The access group audit logging workflow has been manually tested:

- Adding an access group creates an `ADDED` event.
- Removing an access group creates a `REMOVED` event.
- Saving without changing group assignments creates no additional audit entries.
- Audit history appears on the affected user's profile.

Other application workflows should be tested as development continues.

## Project Status

This is an ongoing portfolio project focused on demonstrating practical IT support workflows, basic access administration, database operations, and technical documentation.

Additional security controls, authentication, automated tests, and further operational features may be added as the project evolves.

## Author

**Agustin Brutti**

GitHub: [agustinbrutti19](https://github.com/agustinbrutti19)
