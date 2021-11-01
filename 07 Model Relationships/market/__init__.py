from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from market.database import engine, Base

from market.database import SessionLocal

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

Base.metadata.create_all(engine)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from market import routes