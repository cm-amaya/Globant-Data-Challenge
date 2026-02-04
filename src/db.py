import numpy as np
import pandas as pd
from sqlalchemy import inspect, create_engine
from sqlmodel import SQLModel, Session, create_engine, select
from src.config import settings
from src.models import Employee

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    """Initiate Database, by creating the tables if they do not exists and loading data into them.

    Args:
        session (Session): Database session
    """
    inspector = inspect(engine)
    SQLModel.metadata.drop_all(engine)
    if not inspector.has_table('employee'):
        SQLModel.metadata.create_all(engine)
        load_tables()

def load_tables():
    """ Read the initial CSV files to load the data to databases
    """
    department_df = pd.read_csv(settings.DEPARTMENT_CSV_PATH, 
                                sep=',',
                                header=None,
                                names=['id','department'], 
                                dtype={'id': int, 'department': str})
    jobs_df = pd.read_csv(settings.JOBS_CSV_PATH, 
                          sep=',',
                          header=None,
                          names=['id','job'], 
                          dtype={'id': int, 'job': str})
    employee_df = pd.read_csv(settings.EMPLOYEE_CSV_PATH, 
                              sep=',',
                              header=None,
                              names=['id','name','datetime','department_id','job_id'], 
                              dtype={'id': int, 'name': str,'datetime': str ,'department_id': pd.Int64Dtype(),'job_id':pd.Int64Dtype()})

    try:
        department_df.to_sql('department', engine, if_exists='delete_rows', index=False)
        print(f"Data successfully inserted into department table.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        jobs_df.to_sql('job', engine, if_exists='delete_rows', index=False)
        print(f"Data successfully inserted into job table.")
    except Exception as e:
        print(f"An error occurred: {e}")

    try:
        employee_df.to_sql('employee', engine, if_exists='delete_rows', index=False)
        print(f"Data successfully inserted into employee table.")
    except Exception as e:
        print(f"An error occurred: {e}")