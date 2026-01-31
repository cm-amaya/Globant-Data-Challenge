import sqlalchemy as sa
from sqlmodel import SQLModel
from sqlmodel import Session, create_engine, select
from .config import settings

engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

def init_db(session: Session) -> None:
    """Initiate Database

    Args:
        session (Session): Database session
    """
    alchemy_engine = sa.create_engine(str(settings.SQLALCHEMY_DATABASE_URI))
    insp = sa.inspect(alchemy_engine)
    if insp.has_table("employee", schema=settings.POSTGRES_DB):
        return
    else:
        SQLModel.metadata.create_all(engine)