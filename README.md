# Globant Data Challenge

# Setup Guide

By default, the dependencies are managed with [uv](https://docs.astral.sh/uv/), go there and install it.

From the root folder, you can install all the dependencies with:

```bash
$ uv sync
```



Then you can activate the virtual environment with:

```bash
$ source .venv/bin/activate
```

For local development and testing, a Postgres server must be used. Create an enviroment file (`.env`) with the following enviroment variables, replacing the values for your own:

```bash
POSTGRES_USER="{USER}"
POSTGRES_DB="{DB}"
POSTGRES_PASSWORD="{PASSWORD}"
EMPLOYEE_CSV_PATH="{PATH_TO_CSV}"
DEPARTMENT_CSV_PATH="{PATH_TO_CSV}"
JOBS_CSV_PATH="{PATH_TO_CSV}"
```

Run the FastApi application with the following command:
```bash
uv run uvicorn src.main:app --reload
```

# Run with Docker

Run using Docker compose:

```bash
docker-compose up -d
```