from sqlmodel import Field, Relationship, SQLModel

class Department(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    department: str = Field(default=None)

class Job(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    job: str = Field(default=None)

class Employee(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str | None  = Field(default=None)
    datetime: str | None  = Field(default=None)
    department_id: int | None  = Field(default=None, foreign_key="department.id")
    job_id: int | None = Field(default=None, foreign_key="job.id")
