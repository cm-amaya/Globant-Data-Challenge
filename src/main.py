from fastapi import FastAPI
from sqlmodel import Field, Session, SQLModel, create_engine, select
from .config import settings



engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/")
def read_root():
    return {"Hello": "World"}