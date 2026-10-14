from fastapi import FastAPI, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from app.database import (
    get_open_ticket_count,
    get_recent_tickets,
    get_high_priority_count,
    get_resolved_ticket_count,
    create_ticket,
    get_users,
    get_all_users,
    get_categories,
    get_priorities,
    get_ticket,
    get_all_tickets,
    search_tickets,
    get_tickets_by_status,
    get_ticket_updates,
    get_filtered_tickets,
    get_ticket_escalations,
    create_ticket_update,
    get_statuses,
    update_ticket_status,
    get_ticket_status,
    get_tickets_by_priority,
    get_status_name,
    get_it_users,
    update_ticket_assignment,
    update_ticket,
    get_ticket_assigned_user,
    is_valid_it_user,
    calculate_priority,
    get_impacts,
    get_urgencies,
    count_filtered_tickets,
    get_escalation_teams,
    create_ticket_escalation,
    has_active_escalation,
    resolve_ticket_escalation,
    get_bug_reports,
    create_bug_report,
    get_user_by_id,
    get_user_groups,
    get_user_access,
    get_all_groups,
    update_user_groups,
    get_access_audit_logs,
    get_ticket_status_counts,
    get_critical_open_tickets,
    get_all_access_audit_logs
)
from app.knowledge_base import (
    get_knowledge_base_articles,
    get_knowledge_base_article
)

app = FastAPI()

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")


@app.get("/")
def home(request: Request, ticket_created: int | None = None):
    open_tickets = get_open_ticket_count()
    recent_tickets = get_recent_tickets()
    high_priority = get_high_priority_count()
    resolved_tickets = get_resolved_ticket_count()
    ticket_status_counts = get_ticket_status_counts()
    critical_tickets = get_critical_open_tickets()
    max_ticket_count = max(
        (item["total"] for item in ticket_status_counts),
        default=0
    )

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "open_tickets": open_tickets,
            "recent_tickets": recent_tickets,
            "high_priority": high_priority,
            "resolved_tickets": resolved_tickets,
            "ticket_created": ticket_created,
            "ticket_status_counts": ticket_status_counts,
            "critical_tickets": critical_tickets,
            "max_ticket_count": max_ticket_count
        }
    )

@app.get("/tickets")
def tickets_page(
    request: Request,
    search: str = "",
    status: str = "",
    priority: str = "",
    assigned_to: str = "",
    category: str = "",
    sort: str = "newest",
    page: int = 1
):
    page = max(page, 1)

    statuses = get_statuses()
    priorities = get_priorities()
    it_users = get_it_users()
    categories = get_categories()

    status_id = int(status) if status else None
    priority_id = int(priority) if priority else None
    assigned_to_id = int(assigned_to) if assigned_to else None
    category_id = int(category) if category else None
    tickets_per_page = 10
    offset = (page - 1) * tickets_per_page

    tickets = get_filtered_tickets(
        search=search,
        status_id=status_id,
        priority_id=priority_id,
        assigned_to=assigned_to_id,
        category_id=category_id,
        sort=sort,
        limit=tickets_per_page,
        offset=offset
    )

    total_tickets = count_filtered_tickets(
        search=search,
        status_id=status_id,
        priority_id=priority_id,
        assigned_to=assigned_to_id,
        category_id=category_id
    )

    total_pages = max(
        1,
        (total_tickets + tickets_per_page - 1) // tickets_per_page
    )

    if page > total_pages:
        page = total_pages
        offset = (page - 1) * tickets_per_page

    if total_tickets == 0:
        start_ticket = 0
        end_ticket = 0
    else:
        start_ticket = offset + 1
        end_ticket = min(offset + tickets_per_page, total_tickets)

    return templates.TemplateResponse(
        request=request,
        name="tickets.html",
        context={
            "tickets": tickets,
            "statuses": statuses,
            "priorities": priorities,
            "it_users": it_users,
            "categories": categories,
            "page": page,
            "total_pages": total_pages,
            "total_tickets": total_tickets,
            "start_ticket": start_ticket,
            "end_ticket": end_ticket
        }
    )

@app.get("/new-ticket")
def new_ticket(request: Request):
    users = get_users()
    categories = get_categories()
    priorities = get_priorities()
    impacts = get_impacts()
    urgencies = get_urgencies()

    return templates.TemplateResponse(
        request=request,
        name="new_ticket.html",
        context={
            "users": users,
            "categories": categories,
            "priorities": priorities,
            "impacts": impacts,
            "urgencies": urgencies,
            "categories": categories
        }
    )

@app.get("/users")
def users(request: Request):
    users = get_all_users()

    return templates.TemplateResponse(
        request=request,
        name="users.html",
        context={
            "users": users
        }
    )

@app.get("/audit-logs")
def audit_logs_page(
    request: Request,
    user_name: str = "",
    action: str = "",
    start_date: str = "",
    end_date: str = ""
):
    search_name = user_name.strip()

    selected_action = (
        action if action in ("ADDED", "REMOVED") else None
    )

    selected_start_date = start_date or None
    selected_end_date = end_date or None

    audit_logs = get_all_access_audit_logs(
        user_name=search_name if search_name else None,
        action=selected_action,
        start_date=selected_start_date,
        end_date=selected_end_date
    )

    return templates.TemplateResponse(
        request=request,
        name="audit_logs.html",
        context={
            "audit_logs": audit_logs,
            "user_name": user_name,
            "action": selected_action or "",
            "start_date": start_date,
            "end_date": end_date
        }
    )

@app.get("/users/{user_id}")
def user_detail(user_id: int, request: Request, groups_updated: int = 0):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    groups = get_user_groups(user_id)
    access = get_user_access(user_id)
    all_groups = get_all_groups()
    audit_logs = get_access_audit_logs(user_id)

    return templates.TemplateResponse(
        request=request,
        name="user_detail.html",
        context={
            "user": user,
            "groups": groups,
            "access": access,
            "all_groups": all_groups,
            "groups_updated": groups_updated,
            "audit_logs": audit_logs
        }
    )


@app.post("/users/{user_id}/groups")
def update_user_groups_route(
    user_id: int,
    request: Request,
    group_ids: list[int] = Form(default=[]),
    change_reason: str = Form(min_length=10)
):
    user = get_user_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )
        
    change_reason = change_reason.strip()
    
    if len(change_reason) < 10:
        user = get_user_by_id(user_id)
        groups = get_user_groups(user_id)
        access = get_user_access(user_id)
        all_groups = get_all_groups()
        audit_logs = get_access_audit_logs(user_id)

        return templates.TemplateResponse(
            request=request,
            name="user_detail.html",
            context={
                "user": user,
                "groups": groups,
                "access": access,
                "all_groups": all_groups,
                "groups_updated": 0,
                "audit_logs": audit_logs,
                "error_message": (
                    "The reason must contain at least 10 "
                    "non-whitespace characters."
                )
            },
            status_code=400
        )

    all_groups = get_all_groups()
    valid_group_ids = {group["id"] for group in all_groups}

    if not set(group_ids).issubset(valid_group_ids):
        raise HTTPException(
            status_code=400,
            detail="Invalid access group"
        )

    update_user_groups(user_id, group_ids, change_reason)

    return RedirectResponse(
        url=f"/users/{user_id}?groups_updated=1",
        status_code=303
    )

@app.get("/knowledge-base")
def knowledge_base(request: Request):
    articles = get_knowledge_base_articles()

    search = request.query_params.get("search", "").strip()

    if search:
        search_lower = search.lower()

        articles = [
            article
            for article in articles
            if search_lower in article["id"].lower()
            or search_lower in article["title"].lower()
            or search_lower in article["category"].lower()
            or search_lower in article["system"].lower()
        ]

    return templates.TemplateResponse(
        request=request,
        name="knowledge_base.html",
        context={
            "articles": articles,
            "search": search
        }
    )

@app.get("/knowledge-base/{article_id}")
def knowledge_base_article(article_id: str, request: Request):
    article = get_knowledge_base_article(article_id)

    if article is None:
        raise HTTPException(
            status_code=404,
            detail="Knowledge Base article not found"
        )

    return templates.TemplateResponse(
        request=request,
        name="knowledge_base_article.html",
        context={
            "article": article
        }
    )

@app.get("/tickets/{ticket_id}")
def ticket_detail(request: Request, ticket_id: int):
    ticket = get_ticket(ticket_id)
    updates = get_ticket_updates(ticket_id)
    escalations = get_ticket_escalations(ticket_id)
    bug_reports = get_bug_reports(ticket_id)
    impacts = get_impacts()
    statuses = get_statuses()
    it_users = get_it_users()
    escalation_teams = get_escalation_teams()

    return templates.TemplateResponse(
        request=request,
        name="ticket_detail.html",
        context={
            "ticket": ticket,
            "updates": updates,
            "escalations": escalations,
            "bug_reports": bug_reports,
            "impacts": impacts,
            "statuses": statuses,
            "it_users": it_users,
            "escalation_teams": escalation_teams
        }
    )

@app.post("/tickets/{ticket_id}/bug-reports")
def create_bug_report_route(
    ticket_id: int,
    title: str = Form(...),
    description: str = Form(...),
    steps_to_reproduce: str = Form(...),
    expected_result: str = Form(...),
    actual_result: str = Form(...),
    impact_id: int = Form(...),
    environment: str = Form(...)
):
    bug_report_id = create_bug_report(
        ticket_id,
        title,
        description,
        steps_to_reproduce,
        expected_result,
        actual_result,
        impact_id,
        environment
    )

    create_ticket_update(
        ticket_id,
        7,
        f"Bug Report #{bug_report_id} created: {title}."
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.get("/tickets/{ticket_id}/edit")
def edit_ticket(request: Request, ticket_id: int):
    ticket = get_ticket(ticket_id)

    return templates.TemplateResponse(
        request=request,
        name="edit_ticket.html",
        context={
            "ticket": ticket
        }
    )

@app.post("/tickets/{ticket_id}/edit")
def save_ticket_edit(
    ticket_id: int,
    title: str = Form(...),
    description: str = Form(...)
):
    current_ticket = get_ticket(ticket_id)
    
    changes = []

    if current_ticket["title"] != title:
        changes.append("title")

    if current_ticket["description"] != description:
        changes.append("description")

    if changes:
        change_text = " and ".join(changes)
        history_note = f"Updated ticket {change_text}."

    update_ticket(
        ticket_id,
        title,
        description
    )

    if changes:
        create_ticket_update(
            ticket_id,
            7,
            history_note
        )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/tickets/{ticket_id}/updates")
def add_ticket_update(
    ticket_id: int,
    note: str = Form(...)
):
    create_ticket_update(
        ticket_id,
        7,
        note
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/tickets/{ticket_id}/escalation")
def escalate_ticket(
    ticket_id: int,
    team_id: int = Form(...),
    reason: str = Form(...)
):
    if has_active_escalation(ticket_id):
        return RedirectResponse(
            url=f"/tickets/{ticket_id}",
            status_code=303
        )

    escalation_teams = get_escalation_teams()

    valid_team_ids = [team["id"] for team in escalation_teams]

    if team_id not in valid_team_ids:
        return RedirectResponse(
            url=f"/tickets/{ticket_id}",
            status_code=303
        )

    team_name = None

    for team in escalation_teams:
        if team["id"] == team_id:
            team_name = team["name"]
            break

    create_ticket_escalation(
        ticket_id,
        team_id,
        reason
    )

    create_ticket_update(
        ticket_id,
        7,
        f"Ticket escalated to {team_name}. Reason: {reason}"
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/tickets/{ticket_id}/escalation/resolve")
def resolve_escalation(
    ticket_id: int,
    notes: str = Form(...)
):
    if not has_active_escalation(ticket_id):
        return RedirectResponse(
            url=f"/tickets/{ticket_id}",
            status_code=303
        )

    resolve_ticket_escalation(
        ticket_id,
        notes
    )

    create_ticket_update(
        ticket_id,
        7,
        f"Escalation resolved. Notes: {notes}"
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/tickets/{ticket_id}/status")
def update_status(
    ticket_id: int,
    status_id: int = Form(...)
):
    old_status = get_ticket_status(ticket_id)
    new_status = get_status_name(status_id)

    update_ticket_status(
        ticket_id,
        status_id
    )

    create_ticket_update(
        ticket_id,
        7,
        f"Status changed from {old_status} to {new_status}."
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/tickets/{ticket_id}/assignment")
def update_assignment(
    ticket_id: int,
    assigned_to: int = Form(...)
):
    current_user = get_ticket_assigned_user(ticket_id)
    new_users = get_it_users()

    if not is_valid_it_user(assigned_to):
        return RedirectResponse(
            url=f"/tickets/{ticket_id}",
            status_code=303
        )

    new_user_name = None

    for user in new_users:
        if user["id"] == assigned_to:
            new_user_name = user["name"]
            break

    if current_user["id"] == assigned_to:
        return RedirectResponse(
            url=f"/tickets/{ticket_id}",
            status_code=303
        )

    update_ticket_assignment(
        ticket_id,
        assigned_to
    )

    create_ticket_update(
        ticket_id,
        7,
        f"Ticket assigned from {current_user['name']} to {new_user_name}."
    )

    return RedirectResponse(
        url=f"/tickets/{ticket_id}",
        status_code=303
    )

@app.post("/new-ticket")
def submit_ticket(
    title: str = Form(...),
    description: str = Form(...),
    user_id: int = Form(...),
    category_id: int = Form(...),
    impact_id: int = Form(...),
    urgency_id: int = Form(...)
):
    ticket_id = create_ticket(
        title,
        description,
        user_id,
        category_id,
        impact_id,
        urgency_id
    )

    return RedirectResponse(
        url=f"/?ticket_created={ticket_id}",
        status_code=303
    )



