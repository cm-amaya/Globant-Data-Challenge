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

Create an enviroment file (`.env`) with the following enviroment variables, replacing the values for your own:

```bash
POSTGRES_USER="postgres"
POSTGRES_DB="postgres"
POSTGRES_PORT="5432"
POSTGRES_PASSWORD="{PASSWORD}"
POSTGRES_SCHEMA="public"
EMPLOYEE_CSV_PATH="{PATH_TO_CSV}"
DEPARTMENT_CSV_PATH="{PATH_TO_CSV}"
JOBS_CSV_PATH="{PATH_TO_CSV}"
```

Run the FastApi application with the following command:
```bash
uv run uvicorn src.main:app --reload
```

# Run with Docker

Create the Docker image with the followind command
```bash
docker build -t fastapi-app .
```

Run the Docker image
```bash
docker run --rm --volume .:/app  --volume /app/.venv  --publish 8000:8000 -it $(docker build -q .)
```