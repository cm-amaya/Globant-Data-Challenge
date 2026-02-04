from typing import Annotated

from fastapi import FastAPI, Depends, Query
from sqlmodel import Session, select
from src.db import engine, init_db
from src.config import settings
from src.models import Employee, Job, Department

app = FastAPI(title=settings.app_name)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

@app.on_event("startup")
def on_startup():
    with Session(engine) as session:
        init_db(session)

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/employees/")
def get_employees(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Employee]:
    employees = session.exec(select(Employee).offset(offset).limit(limit)).all()
    return employees

@app.post("/batch_insert/")
def batch_insert(
    session: SessionDep,
    employee_list: list[Employee] = [],
    jobs_list: list[Job] = [],
    department_list: list[Department] = []
):
    for job in jobs_list:
        session.add(job)
    for department in department_list:
        session.add(department)
    for employee in employee_list:
        session.add(employee)
    session.commit()
    return {"Hello": "World"}