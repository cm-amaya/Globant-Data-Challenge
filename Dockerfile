FROM python:3.12-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Copy the project into the image
COPY . /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Disable development dependencies
ENV UV_NO_DEV=1

# Sync the project into a new environment, asserting the lockfile is up to date
WORKDIR /app

# Install the project's dependencies
RUN uv sync --locked

# Ensure the virtual environment bin directory is in the PATH
ENV PATH="/app/.venv/bin:$PATH"

# Expose the port Uvicorn will run on
EXPOSE 8000

# Run the application with Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]