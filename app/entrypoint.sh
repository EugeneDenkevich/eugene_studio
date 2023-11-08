#!/bin/sh
alembic -c /app/src/internal/database/alembic.ini upgrade head

python /app/src/create_roles.py

echo "Starting FastAPI application"
uvicorn app:create_app --host 0.0.0.0 --port 8000 --reload