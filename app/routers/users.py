from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi import Request, status, Form
from app.dependencies import SessionDep
from . import api_router
from app.services.user_service import todoservice
from app.repositories.user import UserRepository
from app.utilities.flash import flash
from app.schemas import UserResponse


# API endpoint for listing todos
@api_router.get("/todos", response_model=list[UserResponse])
async def list_todos(request: Request, db: SessionDep):
    user_repo = UserRepository(db)
    user_service = todoservice(user_repo)
    return user_service.get_all_todos()

from . import api_router

@api_router.get("/todos")
def get_todos():
    return [
        {"id": 1, "title": "Finish lab", "completed": False},
        {"id": 2, "title": "Push to GitHub", "completed": True}
    ]