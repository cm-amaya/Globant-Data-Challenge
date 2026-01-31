from sqlalchemy import inspect
from sqlmodel import SQLModel, Session, create_engine, select
from config import settings
from models import Employee

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    """Initiate Database

    Args:
        session (Session): Database session
    """
    inspector = inspect(engine)
    if not inspector.has_table('employee'):
        SQLModel.metadata.create_all(engine)