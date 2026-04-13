from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from jinja2 import Environment, FileSystemLoader
from app.utilities.flash import get_flashed_messages
from app.config import get_settings

# ---------------------------
# Templates setup
# ---------------------------
template_env = Environment(
    loader=FileSystemLoader("app/templates")
)

template_env.globals["get_flashed_messages"] = get_flashed_messages

templates = Jinja2Templates(env=template_env)

# ---------------------------
# Static files
# ---------------------------
static_files = StaticFiles(directory="app/static")

# ---------------------------
# Routers
# ---------------------------
router = APIRouter(
    tags=["Jinja Based Endpoints"],
    include_in_schema=get_settings().env.lower() in ["dev", "development"]
)

api_router = APIRouter(
    tags=["API Endpoints"],
    prefix="/api"
)

# ---------------------------
# Import route modules
# ---------------------------
from . import (
    index,
    login,
    register,
    admin_home,
    user_home,
    todos,
    logout
)