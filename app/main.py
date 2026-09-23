from fastapi import FastAPI, Request, Form
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
    get_categories,
    get_priorities
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

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "open_tickets": open_tickets,
            "recent_tickets": recent_tickets,
            "high_priority": high_priority,
            "resolved_tickets": resolved_tickets,
            "ticket_created": ticket_created
        }
    )

@app.get("/new-ticket")
def new_ticket(request: Request):
    users = get_users()
    categories = get_categories()
    priorities = get_priorities()

    return templates.TemplateResponse(
        request=request,
        name="new_ticket.html",
        context={
            "users": users,
            "categories": categories,
            "priorities": priorities
        }
    )

@app.post("/new-ticket")
def submit_ticket(
    title: str = Form(...),
    description: str = Form(...),
    user_id: int = Form(...),
    category_id: int = Form(...),
    priority_id: int = Form(...)
):
    ticket_id = create_ticket(
        title,
        description,
        user_id,
        category_id,
        priority_id
    )

    return RedirectResponse(
        url=f"/?ticket_created={ticket_id}",
        status_code=303
    )



