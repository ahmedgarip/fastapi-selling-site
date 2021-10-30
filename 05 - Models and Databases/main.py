
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse

from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import models
from database import engine, SessionLocal

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

models.Base.metadata.create_all(engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse( "home.html", {"request": request})


@app.get("/market", response_class=HTMLResponse)
async def market_page(request: Request):
    items = get_db()

    return templates.TemplateResponse( "market.html", {"request": request, 'items':items})
