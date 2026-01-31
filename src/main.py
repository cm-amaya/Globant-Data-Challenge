from fastapi import FastAPI
from sqlmodel import Session
from db import engine, init_db
from config import settings

app = FastAPI(title=settings.app_name)

@app.on_event("startup")
def on_startup():
    with Session(engine) as session:
        init_db(session)

@app.get("/")
def read_root():
    return {"Hello": "World"}