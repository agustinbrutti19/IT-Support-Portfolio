# IT Support & Helpdesk Lab

A practical IT Support and Helpdesk portfolio project built with Python, FastAPI, SQLite, and Jinja2.

**Live Demo:** [IT Support & Helpdesk Lab](https://it-support-portfolio.onrender.com/)

This project simulates an internal IT environment for **Borealis Travel**, a fictional premium travel company. It demonstrates common IT support workflows, ticket management, user administration, access group auditing, troubleshooting documentation, and ticket escalation.

The application is deployed on Render and can be accessed directly through the live demo without installing or running the project locally.

## Project Objectives

- Simulate day-to-day internal IT support operations.
- Manage helpdesk tickets throughout their lifecycle.
- Calculate ticket priorities based on impact and urgency.
- Manage users, departments, and access groups.
- Track ticket updates and escalations.
- Document software bugs and troubleshooting solutions.
- Maintain an audit trail of access group changes.
- Practice database operations and technical documentation.

## Features

### 1. Dashboard

- Centralized overview of the helpdesk environment.
- Summary of ticket activity and priorities.
- Quick access to the main application sections.

### 2. Ticket Management

- Create, view, and edit support tickets.
- Categorize tickets by issue type.
- Assign priorities based on impact and urgency.
- Track ticket statuses throughout their lifecycle.
- Assign tickets to IT technicians.
- View ticket details and update history.
- Record investigation notes and ticket changes.

### 3. Ticket Escalation

- Escalate tickets to specialized support teams.
- Record escalation details and notes.
- Track issues requiring additional technical support.

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

The application records changes to user access group assignments in the SQLite `access_audit_logs` table.

- Records `ADDED` events when groups are assigned.
- Records `REMOVED` events when groups are removed.
- Identifies the affected user and access group.
- Stores the recorded technician identity.
- Records the date and time of each event.
- Displays audit history on the user's profile.
- Avoids creating audit entries when assignments remain unchanged.

**Current limitation:** The technician identity is simulated as `Alex Carter (IT Support)`. Authentication and automatic identification of the signed-in technician have not been implemented.

### 7. Bug Reporting

- Record software bug reports.
- Document reproduction steps.
- Describe expected and actual results.
- Associate reports with the relevant ticket workflow.

### 8. Knowledge Base

Includes knowledge base articles KB-001 through KB-006 covering common troubleshooting scenarios:

- KB-001: CRM errors when saving customer profiles.
- KB-002: Microsoft 365 login issues.
- KB-003: Zoom microphone troubleshooting.
- KB-004: Shared drive access issues.
- KB-005: Laptop performance troubleshooting.
- KB-006: Windows DNS troubleshooting.

## Technology Stack

- **Python** — application logic.
- **FastAPI** — web framework and routing.
- **SQLite** — relational database.
- **Jinja2** — HTML templating.
- **HTML and CSS** — user interface.
- **pytest** — automated testing.
- **Git and GitHub** — version control and source code hosting.
- **Render** — web application deployment.

## Project Structure

```text
IT-Support-Portfolio/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── knowledge_base.py
│   ├── templates/
│   └── static/
├── database/
│   ├── demo.db
│   ├── init_db.py
│   └── ...
├── docs/
│   ├── company.md
│   ├── users.md
│   ├── user-access-management.md
│   ├── tickets/
│   └── knowledge-base/
├── tests/
│   └── test_priority.py
├── requirements.txt
├── render.yaml
└── README.md
```

The local development database, `database/database.db`, is excluded from version control. The repository includes `database/demo.db` for the deployed demonstration.

## Running the Application Locally

### Prerequisites

- Python 3.13 or a compatible version.
- Git.

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

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Start the development server:

   ```bash
   uvicorn app.main:app --reload
   ```

6. Open the application:

   [http://127.0.0.1:8000](http://127.0.0.1:8000)

### Database Configuration

The application uses the `DATABASE_PATH` environment variable to select its SQLite database.

By default, the application uses `database/database.db`. The deployed service is configured to use `database/demo.db`.

Database initialization scripts should only be run when appropriate for the current database state, as reinitialization may affect existing data.

## Testing and Validation

### Automated Tests

Automated tests using `pytest` cover ticket priority calculation, including:

- All nine combinations of impact and urgency.
- Invalid impact and urgency values.
- Case-insensitive input and whitespace normalization.
- Rejection of non-string values.

Run the tests from the project root:

```bash
python -m pytest tests/test_priority.py -v
```

### Manual Testing

The following workflows have been manually tested:

- Ticket creation, viewing, editing, and status updates.
- Ticket history and escalation workflows.
- User profiles and access group management.
- Access group audit logging for additions and removals.
- Avoidance of duplicate audit entries when assignments remain unchanged.
- Public deployment and ticket category editing.

Testing and validation will continue as the project evolves.

## Deployment

The application is deployed on Render using the configuration in `render.yaml`.

**Live application:** [https://it-support-portfolio.onrender.com/](https://it-support-portfolio.onrender.com/)

The deployment uses the demonstration database and is intended for portfolio evaluation.

**Deployment limitation:** The application uses SQLite, and the free hosting environment may not preserve database changes across restarts or redeployments. The demonstration data can be restored from the repository's `database/demo.db` file.

## Project Status

This is an ongoing portfolio project focused on demonstrating practical IT support workflows, basic access administration, database operations, troubleshooting, and technical documentation.

Authentication, role-based authorization, automated identification of technicians, and additional security controls have not yet been implemented.

## Author

**Agustin Brutti**

- [GitHub Profile](https://github.com/agustinbrutti19)
- [Project Repository](https://github.com/agustinbrutti19/IT-Support-Portfolio)
- [Live Demo](https://it-support-portfolio.onrender.com/)
