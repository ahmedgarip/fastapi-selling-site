from starlette.templating import Jinja2Templates

from market import app, get_db
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse


templates = Jinja2Templates(directory="market/templates")

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse( "home.html", {"request": request})


@app.get("/market", response_class=HTMLResponse)
async def market_page(request: Request):
    items = get_db()

    return templates.TemplateResponse( "market.html", {"request": request, 'items':items})